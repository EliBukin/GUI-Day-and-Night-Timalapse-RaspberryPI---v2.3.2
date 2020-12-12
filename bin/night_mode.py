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

dest_photo_night = configfile['path_vars']['ndest_photo_night']
dest_location = configfile['path_vars']['dest_location']
ineligible_files = configfile['path_vars']['ineligible_files']
night_interval = configfile['night_config']['ninterval']
night_light_low_limit = configfile['night_config']['nlight_low_limit']
cam_resolution = configfile['camera_parameters']['resolution']

string_from_configfile = cam_resolution

### converting the string from configfile to tuple that will be used in the timelapse loop
# using map() + tuple() + int + split()
res = tuple(map(int, string_from_configfile.split(', ')))

# printing result
#print("Tuple after getting conversion from String : " + str(res))
cam_resolution1 = res

### Night Mode
def night_mode():
   camera = PiCamera(resolution=(cam_resolution1), framerate=Fraction(1, 6))
   camera.shutter_speed = 6000000
   camera.iso = 800
   # Give the camera a good long time to set gains and
   # measure AWB (you may wish to use fixed AWB instead)
   sleep(5)
   camera.exposure_mode = 'off'
   # Finally, capture an image with a 6s exposure. Due
   # to mode switching on the still port, this will take
   # longer than 6 seconds
   ###
   for filename in camera.capture_continuous(dest_photo_night+'night '+'{timestamp:%a-%d.%m.%Y-%H-%M-%S}'+'_{counter:05d}.jpg'):
      print('[INFO]: NM Captured %s' % filename)
      time.sleep(night_interval) # interval in seconds
      check_light(dest_photo_night+'*')
      print ('[INFO]: light is ' + str(check_light.light))
      if check_light.light < night_light_low_limit:
         print ('[INFO]: '+(check_light.img +' is a night photo'))
      else:
         print ("Too bright for Night Mode, exiting...")
         break

night_mode()
