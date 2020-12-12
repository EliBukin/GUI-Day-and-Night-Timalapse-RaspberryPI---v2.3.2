#!/usr/bin/python3

import time
import picamera
import yaml
import sys

### defines arguments as variables
configfile_location = (sys.argv[1])
#
with open(configfile_location, "r") as ymlfile:
   configfile = yaml.safe_load(ymlfile)

cam_resolution = configfile['camera_parameters']['resolution']
string_from_configfile = cam_resolution

### converting the string from configfile to tuple that will be used in the timelapse loop  
# using map() + tuple() + int + split() 
res = tuple(map(int, string_from_configfile.split(', '))) 

cam_resolution1 = res

###
with picamera.PiCamera() as camera:
    camera.resolution = (cam_resolution1)
    camera.start_preview()
    time.sleep(120)
    camera.stop_preview()
