#ifndef __DECODE_GIF_H__
#define __DECODE_GIF_H__

#include <assert.h>
#include <errno.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>

#ifdef __cplusplus
extern "C" {
#endif

#include <libnsgif.h>
#include <decode_gif.h>

void *bitmap_create(int width, int height);
void bitmap_set_opaque(void *bitmap, bool opaque);
bool bitmap_test_opaque(void *bitmap);
unsigned char *bitmap_get_buffer(void *bitmap);
void bitmap_destroy(void *bitmap);
void bitmap_modified(void *bitmap);

typedef struct {
	gif_animation animation;
	gif_bitmap_callback_vt bitmap_callbacks;
	unsigned char* data;
} GIF;

GIF* gif_new();
void gif_init(GIF* gif);
int gif_load_file(GIF* gif, const char* filename);
unsigned char* gif_get_frame(GIF* gif, int frame_number);
void gif_free(GIF* gif);
void gif_free_content(GIF* gif);

#ifdef __cplusplus
}
#endif

#endif