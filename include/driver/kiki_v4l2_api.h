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

#ifndef KIKI_V4L2_API
#define KIKI_V4L2_API

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <sys/mman.h>
#include <sys/ioctl.h>
#include <linux/videodev2.h>

#include "kiki_image_types.h"

#ifdef __cplusplus
extern "C" {
#endif

struct buffer {
	void* start;
	size_t length;
};

typedef int device_fd_t;
typedef int device_id_t;
typedef unsigned char raw_t;

typedef struct {
	device_fd_t device_fd;
	int buffers_amount;
	struct buffer* buffers;
	image_size_t image_size;
	char* device_path;

	void (*image_treatment)(image_size_t image_size, raw_t *dst, raw_t *src);
} device_handle_t;

raw_t *kiki_v4l2_allocate_image_data(device_handle_t *device_handle);
int kiki_v4l2_capture_frame(device_handle_t*, raw_t *dst);

int kiki_v4l2_open_device(device_handle_t*, const char *path, int width, int height);
int kiki_v4l2_close_device(device_handle_t*);
int kiki_v4l2_turn_device_on(device_handle_t*);
int kiki_v4l2_turn_device_off(device_handle_t*);

int kiki_v4l2_reset_parameter(device_handle_t* device_handle, int v4l2_parameter);
int kiki_v4l2_set_parameter(device_handle_t* device_handle, int v4l2_parameter, int value);
int kiki_v4l2_get_parameter(device_handle_t* device_handle, int v4l2_parameter, int* value);

void kiki_v4l2_default_image_treatment(image_size_t image_size, raw_t *dst, raw_t *src);
void kiki_v4l2_YUV422toRGB888(image_size_t image_size, raw_t *dst, raw_t *src);
void kiki_v4l2_YUV422toBGR888(image_size_t image_size, raw_t *dst, raw_t *src);

#ifdef __cplusplus
}
#endif

#endif