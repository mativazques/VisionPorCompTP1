#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

drawing = False  # true if mouse is pressed
ix, iy = -1, -1
fx, fy = -1, -1
 
img = cv2.imread('images\image.jpg')
img2 = cv2.imread('images\image.jpg')

def draw_rectangle(event, x, y, flags, param):
 global ix, iy, fx, fy, drawing
 
 if event == cv2.EVENT_LBUTTONDOWN:
  drawing = True
  ix, iy = x, y
        
 elif event == cv2.EVENT_MOUSEMOVE:
  if drawing is True:
   cv2.rectangle(img2, (ix, iy), (x, y), (0, 255, 0), -1)
            
 elif event == cv2.EVENT_LBUTTONUP:
  
  drawing = False
  cv2.rectangle(img2, (ix, iy), (x, y), (0, 255, 0), -1)
  fx, fy = x, y        

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

def save_image():
 global ix, iy, fx, fy
 crop_img = img[iy:fy,ix:fx]
 cv2.imwrite('images\resultado_tp1.png', crop_img)
 print("Imagen recortada guardada!")
 
 
def reset_image():
 print("Imagen restablecida!")


while(1):
 cv2.imshow('image', img2)
 k = cv2.waitKey(1) & 0xFF
 if k == ord('g'):
  save_image()
  break
     
 elif k == ord('r'):
  img2 = img
  img = cv2.imread('images\image.jpg')
  reset_image()
  
 elif k == ord('q'):
  break
cv2.destroyAllWindows()