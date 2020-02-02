# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:58:08 2019

@author: mante
"""

#from matplotlib import pyplot as plt
from skimage.io import imread
from skimage.io import imsave
from skimage.measure import compare_ssim 
from skimage.viewer import ImageViewer

rgb_image = imread("Market_RGB.png")
rgb_image.shape

# Red
red_image = rgb_image.copy() # Make a copy
red_image[:,:,1] = 0
red_image[:,:,2] = 0
imsave("Market_R.png",red_image)
#R_viewer = ImageViewer(red_image)
#R_viewer.show()

# Green
green_image = rgb_image.copy() # Make a copy
green_image[:,:,0] = 0
green_image[:,:,2] = 0
imsave("Market_G.png",green_image)
#G_viewer = ImageViewer(green_image)
#G_viewer.show()

# Blue
blue_image = rgb_image.copy() # Make a copy
blue_image[:,:,0] = 0
blue_image[:,:,1] = 0
imsave("Market_B.png",blue_image)
#B_viewer = ImageViewer(blue_image)
#B_viewer.show()

#imsave("Market_G.png",green_image)

#img_width = len(img_target[0])
#img_height = len(img_target)
#
#img_left = round(img_width/2 - img_height/2)
#img_right = round(img_width/2 + img_height/2)
#img_bottom = img_height*0
#img_top = img_height
#
#img_target_cut = img_target[img_bottom:img_top,img_left:img_right]
#
#SSIM_max=0
#
#for i in range(1, 9):
#
#    filenum = (str(i))
#    filename = ("f" + filenum + ".png")
#    img_compare = imread(filename);
#    img_compare_cut = img_compare[img_bottom:img_top,img_left:img_right]
#    
#    SSIM = compare_ssim(img_target_cut, img_compare_cut,multichannel=True)
#    
#    print(i)
#    print(SSIM)
#
#    if SSIM>SSIM_max:
#        SSIM_max=SSIM
#        i_max=i
#        filename_max=filename
#        
#print()
#print("The most similar image is ",filename_max,"( #",i_max,") with SSIM =",SSIM_max)
