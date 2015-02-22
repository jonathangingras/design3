/* Copyright (c) 2014, Jonathan Gingras
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without modification, 
 * are permitted provided that the following conditions are met:
 * 
 * 1. Redistributions of source code must retain the above copyright notice,
 *    this list of conditions and the following disclaimer.
 * 
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.  
 */

/* 
 * based on http://linuxtv.org/downloads/v4l-dvb-apis/capture-example.html
 */
#include <kiki_v4l2_api.h>

#define PERROR_AND_RETURN(err_str, ...) {\
  fprintf(stderr, "[errno: %d, msg: %s] --> [function msg: "err_str"]\n",\
    errno, (errno ? strerror(errno) : "(null)"), ##__VA_ARGS__);\
    return -1;\
  }

#define memsafeclean(x) memset (&(x), 0, sizeof (x))

void kiki_v4l2_default_image_treatment(image_size_t image_size, raw_t *dst, raw_t *src) {
  memcpy(dst, src, image_size.width * image_size.height);
}

static int xioctl(device_fd_t device_fd, int request, void* argp) {
  int result;

  do {
    result = ioctl(device_fd, request, argp);
  } while(result == -1 && errno == EINTR);

  return result;
}

#define DEVICE_FRAME_GOT_IT     0
#define DEVICE_FRAME_TRY_AGAIN  1
#define DEVICE_FRAME_ERROR     -1

static int read_frame(raw_t *dst, device_handle_t *device_handle) {
  struct v4l2_buffer buf;
  memsafeclean(buf);

  buf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
  buf.memory = V4L2_MEMORY_MMAP;

  if(xioctl(device_handle->device_fd, VIDIOC_DQBUF, &buf) == -1) {
    switch (errno) {
      case EAGAIN:
        return DEVICE_FRAME_TRY_AGAIN;
      case EIO:
      default:
        return DEVICE_FRAME_ERROR;
    }
  }

  if(buf.index >= device_handle->buffers_amount) return DEVICE_FRAME_ERROR;

  /*apply the image treatment to yuv422 data*/
  device_handle->image_treatment(
    device_handle->image_size, 
    dst, 
    (raw_t*)(device_handle->buffers)[buf.index].start
  );

  if (xioctl(device_handle->device_fd, VIDIOC_QBUF, &buf) == -1) {
    return DEVICE_FRAME_ERROR;
  }

  return DEVICE_FRAME_GOT_IT;
}

static int stop_capture(device_handle_t *device_handle) {
  enum v4l2_buf_type type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
  if (xioctl(device_handle->device_fd, VIDIOC_STREAMOFF, &type) == -1) return -1;
  
  return 0;
}

static int start_capture(device_handle_t *device_handle) {
  unsigned int i;
  enum v4l2_buf_type type;

  for (i = 0; i < device_handle->buffers_amount; ++i) {
    struct v4l2_buffer buf;

    memsafeclean(buf);

    buf.type        = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    buf.memory      = V4L2_MEMORY_MMAP;
    buf.index       = i;

    if (xioctl(device_handle->device_fd, VIDIOC_QBUF, &buf) == -1) return -1;
  }
                
  type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
  if (xioctl(device_handle->device_fd, VIDIOC_STREAMON, &type) == -1) return -1;

  return 0;
}

static int free_buffers(device_handle_t *device_handle) {
  unsigned int i;
  for (i = 0; i < device_handle->buffers_amount; ++i)
    if (-1 == munmap (device_handle->buffers[i].start, device_handle->buffers[i].length))
      return -1;

  free(device_handle->buffers);
  return 0;
}

static int init_mmap(device_handle_t *device_handle) {
  struct v4l2_requestbuffers request_buffers;

  memsafeclean(request_buffers);

  request_buffers.count = 4;
  request_buffers.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
  request_buffers.memory = V4L2_MEMORY_MMAP;

  if (xioctl(device_handle->device_fd, VIDIOC_REQBUFS, &request_buffers) == -1) {
    if (EINVAL == errno) {
      PERROR_AND_RETURN("device %s does not support memory mapping\n", device_handle->device_path);
    } else {
      PERROR_AND_RETURN("VIDIOC_REQBUFS");
    }
  }

  if (request_buffers.count < 2) {
    PERROR_AND_RETURN("insufficient buffer memory on device %s\n", device_handle->device_path);
  }

  (device_handle->buffers) = (struct buffer*)calloc(request_buffers.count, sizeof(*(device_handle->buffers)));

  if(!(device_handle->buffers)) {
    PERROR_AND_RETURN("out of memory\n");
  }

  for (device_handle->buffers_amount = 0; device_handle->buffers_amount < request_buffers.count; ++device_handle->buffers_amount) {
    struct v4l2_buffer buf;

    memsafeclean(buf);

    buf.type        = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    buf.memory      = V4L2_MEMORY_MMAP;
    buf.index       = device_handle->buffers_amount;

    if (xioctl(device_handle->device_fd, VIDIOC_QUERYBUF, &buf) == -1) {
      PERROR_AND_RETURN("VIDIOC_QUERYBUF");
    }

    device_handle->buffers[device_handle->buffers_amount].length = buf.length;
    device_handle->buffers[device_handle->buffers_amount].start =
    mmap (NULL, buf.length, PROT_READ | PROT_WRITE, MAP_SHARED, device_handle->device_fd, buf.m.offset);

    if ((device_handle->buffers)[device_handle->buffers_amount].start == MAP_FAILED) {
      PERROR_AND_RETURN("could not initiate mmap");
    }
  }

  return 0;
}

static int init_device(device_handle_t *device_handle) {
  struct v4l2_capability cap;
  struct v4l2_cropcap cropcap;
  struct v4l2_crop crop;
  struct v4l2_format fmt;
  unsigned int min;

  if (xioctl(device_handle->device_fd, VIDIOC_QUERYCAP, &cap) == -1) {
    if (EINVAL == errno) {
      PERROR_AND_RETURN("device %s is not a V4L2 device\n", device_handle->device_path);
    } else {
      PERROR_AND_RETURN("VIDIOC_QUERYCAP");
    }
  }

  if (!(cap.capabilities & V4L2_CAP_VIDEO_CAPTURE)) {
    PERROR_AND_RETURN("device %s is not a video capture device\n", device_handle->device_path);
  }

  if (!(cap.capabilities & V4L2_CAP_STREAMING)) {
    PERROR_AND_RETURN("device %s does not support streaming i/o\n", device_handle->device_path);
  }


  /* Select video input, video standard and tune here. */
  memsafeclean(cropcap);

  cropcap.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;

  if (xioctl(device_handle->device_fd, VIDIOC_CROPCAP, &cropcap) == 0) {
    crop.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    crop.c = cropcap.defrect; /* reset to default */

    xioctl(device_handle->device_fd, VIDIOC_S_CROP, &crop);
  }

  memsafeclean(fmt);

  // v4l2_format
  fmt.type                = V4L2_BUF_TYPE_VIDEO_CAPTURE;
  fmt.fmt.pix.width       = device_handle->image_size.width; 
  fmt.fmt.pix.height      = device_handle->image_size.height;
  fmt.fmt.pix.pixelformat = V4L2_PIX_FMT_YUYV;
  fmt.fmt.pix.field       = V4L2_FIELD_INTERLACED;

  if (xioctl(device_handle->device_fd, VIDIOC_S_FMT, &fmt) == -1) 
    PERROR_AND_RETURN("VIDIOC_S_FMT");

  /* Note VIDIOC_S_FMT may change width and height. */
  if (device_handle->image_size.width != fmt.fmt.pix.width) {
    device_handle->image_size.width = fmt.fmt.pix.width;
    fprintf(stderr,"Image width set to %i by device %s.\n", device_handle->image_size.width, device_handle->device_path);
  }
  if (device_handle->image_size.height != fmt.fmt.pix.height) {
    device_handle->image_size.height = fmt.fmt.pix.height;
    fprintf(stderr,"Image height set to %i by device %s.\n", device_handle->image_size.height, device_handle->device_path);
  }

  /* Buggy driver paranoia. */
  min = fmt.fmt.pix.width * 2;
  if (fmt.fmt.pix.bytesperline < min)
    fmt.fmt.pix.bytesperline = min;
  min = fmt.fmt.pix.bytesperline * fmt.fmt.pix.height;
  if (fmt.fmt.pix.sizeimage < min)
    fmt.fmt.pix.sizeimage = min;

  return init_mmap(device_handle);
}

static device_fd_t open_device_fd(const char *deviceName) {
  struct stat st;

  if (-1 == stat(deviceName, &st)) {
    PERROR_AND_RETURN("cannot find '%s': %d, %s\n", deviceName, errno, strerror (errno));
  }

  if (!S_ISCHR (st.st_mode)) {
    PERROR_AND_RETURN("%s is not a device\n", deviceName);
  }

  device_fd_t device_fd = open(deviceName, O_RDWR | O_NONBLOCK, 0);

  if (-1 == device_fd) {
    PERROR_AND_RETURN("could not open '%s': %d, %s\n", deviceName, errno, strerror (errno));
  }

  return device_fd;
}

static int kiki_v4l2_set_parameter_intern(device_handle_t* device_handle, int v4l2_parameter, int value, int to_default) {
  struct v4l2_queryctrl queryctrl;
  memsafeclean(queryctrl);
  struct v4l2_control control;
  memsafeclean(control);

  queryctrl.id = v4l2_parameter;

  control.id = v4l2_parameter;

  if (-1 == ioctl(device_handle->device_fd, VIDIOC_QUERYCTRL, &queryctrl)) {
    if (errno != EINVAL) {
      PERROR_AND_RETURN("could not execute VIDIOC_QUERYCTRL");
    } else {
      PERROR_AND_RETURN("V4L2 parameter is not supported (ioctl returned -1)\n");
    }
  } else if (queryctrl.flags & V4L2_CTRL_FLAG_DISABLED) {
      PERROR_AND_RETURN("V4L2 parameter is not supported (query flag was set to disabled)\n");
  } else {
    control.value = (to_default ? queryctrl.default_value : value);

    if (-1 == ioctl(device_handle->device_fd, VIDIOC_S_CTRL, &control)) {
      PERROR_AND_RETURN("could not execute VIDIOC_S_CTRL");
    }
  }
  return 0;
}

////////////////////////// PUBLIC API //////////////////////////////

int kiki_v4l2_capture_frame(device_handle_t *device_handle, raw_t *dst) {
  int result;
  do {
    fd_set fds;
    struct timeval tv;
    int r;

    FD_ZERO(&fds);
    FD_SET(device_handle->device_fd, &fds);

    /* Timeout. */
    tv.tv_sec = 2;
    tv.tv_usec = 0;

    r = select(device_handle->device_fd + 1, &fds, NULL, NULL, &tv);

    if (r == -1) {
      if(EINTR == errno) continue;
      else return -1;
    }

    if (r == 0) {
      PERROR_AND_RETURN("select() has timed out\n");
    }

    result = read_frame(dst, device_handle);
    if(result == DEVICE_FRAME_ERROR) break;

  } while(result);

  return result;
}

raw_t *kiki_v4l2_allocate_image_data(device_handle_t *device_handle) {
  return (raw_t*)malloc(device_handle->image_size.width * device_handle->image_size.height * 3 * sizeof(char));
}

int kiki_v4l2_open_device(device_handle_t *device_handle, const char *device_path, int image_width, int image_height) {
  device_handle->device_path = (char*)calloc(strlen(device_path) + 1, sizeof(char));
  if(!device_handle->device_path) PERROR_AND_RETURN("could not allocate space for device name");

  strcat(device_handle->device_path, device_path);
  
  device_handle->image_size = (image_size_t){image_width, image_height};
  device_handle->device_fd = open_device_fd(device_handle->device_path);
  
  if(device_handle->device_fd == -1) PERROR_AND_RETURN("could not open device file descriptor");

  device_handle->image_treatment = &kiki_v4l2_default_image_treatment;

  return 0;
}

int kiki_v4l2_close_device(device_handle_t *device_handle) {
  if (close(device_handle->device_fd) == -1) PERROR_AND_RETURN("could not close device");
  device_handle->device_fd = -1;
  free(device_handle->device_path);
  return 0;
}

int kiki_v4l2_turn_device_on(device_handle_t *device_handle) {
  if(init_device(device_handle)) PERROR_AND_RETURN("could not initiate device");
  if(start_capture(device_handle)) PERROR_AND_RETURN("could not start capturing from device");
  return 0;
}

int kiki_v4l2_turn_device_off(device_handle_t *device_handle) {
  if(stop_capture(device_handle)) PERROR_AND_RETURN("could not stop capturing from device");
  if(free_buffers(device_handle)) PERROR_AND_RETURN("could not close mmap when freeing buffers");
  return 0;
}

int kiki_v4l2_reset_parameter(device_handle_t* device_handle, int v4l2_parameter) {
  return kiki_v4l2_set_parameter_intern(device_handle, v4l2_parameter, 0, 1);
}

int kiki_v4l2_set_parameter(device_handle_t* device_handle, int v4l2_parameter, int value) {
  return kiki_v4l2_set_parameter_intern(device_handle, v4l2_parameter, value, 0);
}

int kiki_v4l2_get_parameter(device_handle_t* device_handle, int v4l2_parameter, int* value) {
  struct v4l2_queryctrl queryctrl;
  memsafeclean(queryctrl);
  struct v4l2_control control;
  memsafeclean(control);

  queryctrl.id = v4l2_parameter;

  control.id = v4l2_parameter;

  if (-1 == ioctl(device_handle->device_fd, VIDIOC_QUERYCTRL, &queryctrl)) {
    if (errno != EINVAL) {
      PERROR_AND_RETURN("VIDIOC_QUERYCTRL");
    } else {
      PERROR_AND_RETURN("V4L2 parameter is not supported (ioctl returned -1)\n");
    }
  } else if (queryctrl.flags & V4L2_CTRL_FLAG_DISABLED) {
      PERROR_AND_RETURN("V4L2 parameter is not supported (query flag was set to disabled)\n");
  } else {
    if (-1 == ioctl(device_handle->device_fd, VIDIOC_G_CTRL, &control)) {
      PERROR_AND_RETURN("VIDIOC_S_CTRL");
    }
    *value = control.value;
  }
  return 0;
}