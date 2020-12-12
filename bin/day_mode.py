#!/usr/bin/python3

import time
import picamera
from picamera import PiCamera
from fractions import Fraction
import sys
from check_light_func import check_light
from time import sleep
from datetime import datetime
import yaml
# to move the ineligible file
import os
import shutil

### defines arguments as variables
configfile_location = (sys.argv[1])
#
with open(configfile_location, "r") as ymlfile:
   configfile = yaml.safe_load(ymlfile)

dest_photo_day = configfile['path_vars']['ddest_photo_day']
dest_location = configfile['path_vars']['dest_location']
ineligible_files = configfile['path_vars']['ineligible_files']
day_interval = configfile['day_config']['dinterval']
day_light_low_limit = configfile['day_config']['dlight_low_limit']
cam_resolution = configfile['camera_parameters']['resolution']

string_from_configfile = cam_resolution

### converting the string from configfile to tuple that will be used in the timelapse loop
# using map() + tuple() + int + split()
res = tuple(map(int, string_from_configfile.split(', ')))

# printing result
#print("Tuple after getting conversion from String : " + str(res))
cam_resolution1 = res

### Day Mode
def day_mode():
      camera = PiCamera(resolution=(cam_resolution1))
      time.sleep(2)
      for filename in camera.capture_continuous(dest_photo_day+'day '+'{timestamp:%a-%d.%m.%Y-%H-%M-%S}'+'_{counter:05d}.jpg'):
         print ('[INFO]: DM Captured %s' % filename)
         time.sleep(day_interval) # interval in seconds
         check_light(dest_photo_day+'*')
         print ('[INFO]: light is ' + str(check_light.light))
         if check_light.light < day_light_low_limit:
            print ("Too dark for Day Mode, exiting...")
            break
         else:
            print ('[INFO]: '+(check_light.img +' is a day photo'))
            
day_mode()
