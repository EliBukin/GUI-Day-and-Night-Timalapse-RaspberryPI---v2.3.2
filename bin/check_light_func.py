#!/usr/bin/python3

import glob
import os
import time
from PIL import Image, ImageStat
import math
#
import sys

def check_light(image):
   # gets the latest file from the list of files
   list_of_files = glob.glob(image) # * means all, if need specific format then *.csv
   latest_file = max(list_of_files, key=os.path.getctime)

   imgFile = latest_file

   # brigtness functions inspired by:
   # http://www.trevorappleton.blogspot.co.uk/2013/11/creating-time-lapse-camera-with.html

   #Covert image to greyscale, return average pixel brightness
   def brightness_GreyScaleMean():
      im = Image.open(imgFile).convert('L')
      stat = ImageStat.Stat(im)
      return stat.mean[0]

   #Covert image to greyscale, return RMS pixel brightness.
   def brightness_GreyScaleRMS():
      im = Image.open(imgFile).convert('L')
      stat = ImageStat.Stat(im)
      return stat.rms[0]

   #Average pixels, then transform to "perceived brightness".
   def brightness_Perceived():
      im = Image.open(imgFile)
      stat = ImageStat.Stat(im)
      r,g,b = stat.mean
      return math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))

   summ_of_all_three = brightness_GreyScaleMean()+brightness_GreyScaleRMS()+brightness_Perceived()
   summ_of_all_three_int = int(summ_of_all_three)
   check_light.light = summ_of_all_three_int
   check_light.img = imgFile
