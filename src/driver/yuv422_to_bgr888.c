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
 * based on http://en.wikipedia.org/wiki/YUV
 */
#include <kiki_v4l2_api.h>

#define WRAP2FF(x) ( (x)>=0xFF ? 0xFF : ( (x) <= 0x00 ? 0x00 : (x) ) )

void kiki_v4l2_YUV422toBGR888(image_size_t image_size, raw_t *dst, raw_t *src) {
  int line, column;
  raw_t *y, *u, *v;

  y = src;
  u = src + 1;
  v = src + 3;

  for (line = 0; line < image_size.height; ++line) {
    for (column = 0; column < image_size.width; ++column) {
      *(dst + 2) = WRAP2FF((double)*y + 1.402 * ((double)*v - 128.0));
      *(dst + 1) = WRAP2FF((double)*y - 0.344 * ((double)*u - 128.0) - 0.714 * ((double)*v - 128.0));      
      *(dst) = WRAP2FF((double)*y + 1.772 * ((double)*u - 128.0));

      dst += 3;

      // increase y every time
      y += 2;
      
      // increase u,v every second time
      if ((column & 1) == 1) {
        u += 4;
        v += 4;
      }
    }
  }
}