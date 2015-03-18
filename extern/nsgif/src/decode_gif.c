/*
 * Copyright 2008 Sean Fox <dyntryx@gmail.com>
 * Copyright 2008 James Bursa <james@netsurf-browser.org>
 *
 * This file is part of NetSurf's libnsgif, http://www.netsurf-browser.org/
 * Licenced under the MIT License,
 *                http://www.opensource.org/licenses/mit-license.php
 */

#include <decode_gif.h>

static unsigned char *load_file(const char *path, size_t *data_size);
static void warning(const char *context, int code);

GIF* gif_new() {
	GIF* gif = (GIF*)malloc(sizeof(GIF));
	if(!gif) {
		return NULL;
	}
	gif_init(gif);
	return gif;
}

void gif_init(GIF* gif) {
	gif->bitmap_callbacks = (gif_bitmap_callback_vt){
		bitmap_create,
		bitmap_destroy,
		bitmap_get_buffer,
		bitmap_set_opaque,
		bitmap_test_opaque,
		bitmap_modified
	};
	//gif->animation = animation;
}

int gif_load_file(GIF* gif, const char* filename) {
	size_t size;
	gif_result code;
	unsigned int i;

	/* create our gif animation */
	gif_create(&gif->animation, &gif->bitmap_callbacks);

	/* load file into memory */
	gif->data = load_file(filename, &size);

	/* begin decoding */
	do {
		code = gif_initialise(&gif->animation, size, gif->data);
		if (code != GIF_OK && code != GIF_WORKING) {
			warning("gif_initialise", code);
			return -1;
		}
	} while (code != GIF_OK);

	return 0;
}

unsigned char* gif_get_frame(GIF* gif, int frame_number) {
		gif_result code;
		code = gif_decode_frame(&gif->animation, frame_number);
		if (code != GIF_OK)
			warning("gif_decode_frame", code);

		return (unsigned char *) gif->animation.frame_image;
}

void gif_free_content(GIF* gif) {
	gif_finalise(&gif->animation);
	free(gif->data);
}

void gif_free(GIF* gif) {
	gif_free_content(gif);
	free(gif);
}

unsigned char *load_file(const char *path, size_t *data_size)
{
	FILE *fd;
	struct stat sb;
	unsigned char *buffer;
	size_t size;
	size_t n;

	fd = fopen(path, "rb");
	if (!fd) {
		perror(path);
		exit(EXIT_FAILURE);
	}

	if (stat(path, &sb)) {
		perror(path);
		exit(EXIT_FAILURE);
	}
	size = sb.st_size;

	buffer = malloc(size);
	if (!buffer) {
		fprintf(stderr, "Unable to allocate %lld bytes\n",
				(long long) size);
		exit(EXIT_FAILURE);
	}

	n = fread(buffer, 1, size, fd);
	if (n != size) {
		perror(path);
		exit(EXIT_FAILURE);
	}

	fclose(fd);

	*data_size = size;
	return buffer;
}


void warning(const char *context, gif_result code)
{
	fprintf(stderr, "%s failed: ", context);
	switch (code)
	{
	case GIF_INSUFFICIENT_FRAME_DATA:
		fprintf(stderr, "GIF_INSUFFICIENT_FRAME_DATA");
		break;
	case GIF_FRAME_DATA_ERROR:
		fprintf(stderr, "GIF_FRAME_DATA_ERROR");
		break;
	case GIF_INSUFFICIENT_DATA:
		fprintf(stderr, "GIF_INSUFFICIENT_DATA");
		break;
	case GIF_DATA_ERROR:
		fprintf(stderr, "GIF_DATA_ERROR");
		break;
	case GIF_INSUFFICIENT_MEMORY:
		fprintf(stderr, "GIF_INSUFFICIENT_MEMORY");
		break;
	default:
		fprintf(stderr, "unknown code %i", code);
		break;
	}
	fprintf(stderr, "\n");
}


void *bitmap_create(int width, int height)
{
	return calloc(width * height, 4);
}


void bitmap_set_opaque(void *bitmap, bool opaque)
{
	(void) opaque;  /* unused */
	assert(bitmap);
}


bool bitmap_test_opaque(void *bitmap)
{
	assert(bitmap);
	return false;
}


unsigned char *bitmap_get_buffer(void *bitmap)
{
	assert(bitmap);
	return bitmap;
}


void bitmap_destroy(void *bitmap)
{
	assert(bitmap);
	free(bitmap);
}


void bitmap_modified(void *bitmap)
{
	assert(bitmap);
	return;
}

