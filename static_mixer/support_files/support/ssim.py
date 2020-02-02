# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:58:08 2019

@author: mante
"""

from skimage.io import imread
from skimage.measure import compare_ssim 

img_target = imread("target.png")



#To plot image using matplotlib
from skimage import data, io
from matplotlib import pyplot as plt
#io.imshow(img_target)
#plt.show()



img_width = len(img_target[0])
img_height = len(img_target)

#cut_factor = 2
#img_left = round(img_width/cut_factor - img_height/cut_factor)
#img_right = round(img_width/cut_factor + img_height/cut_factor)
#img_bottom = img_height*0
#img_top = img_height

img_left = 150
img_right = 650 
img_bottom = 0
img_top = 600

img_target_cut = img_target[img_bottom:img_top,img_left:img_right]

#Plot target image after cut
#io.imshow(img_target_cut)
#plt.show()


SSIM_max=0

filename = ("fnobar.png")
img_compare = imread(filename);
img_compare_cut = img_compare[img_bottom:img_top,img_left:img_right]

SSIM = compare_ssim(img_target_cut, img_compare_cut,multichannel=True)
print(SSIM)

s0 = str(SSIM)
with open('SSIM_out.txt','w') as f:
    #f.write('%f' % SSIM)
    f.write(s0)

f.close()
