#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import subprocess
import os
import yaml

fname = "cam_configfile.yaml"

### variables from configfile
with open(fname, "r") as ymlfile:
   configfile = yaml.safe_load(ymlfile)

current_day_value_in_configfile = configfile['day_config']['dinterval']
current_night_value_in_configfile = configfile['night_config']['ninterval']
current_resolution = configfile['camera_parameters']['resolution']
current_day_light_limit = configfile['day_config']['dlight_low_limit']
current_night_light_limit = configfile['night_config']['nlight_low_limit']
current_day_destination_path = configfile['path_vars']['ddest_photo_day']
current_night_destination_path = configfile['path_vars']['ndest_photo_night']
current_ineligible_files_path = configfile['path_vars']['ineligible_files']

###
top = Tk()
top.geometry("800x540")
top.resizable(width=False, height=False)
top.title("Pi Camera TimeLapse Tool V2.3.2")

### frame
labelframe = LabelFrame(top, text = "Day and Night Time Lapse configuration", width=250, height=80)
labelframe.pack(fill = "both", expand = "yes")

### caption (authors values interval)
var = StringVar()
label = Label( top, textvariable=var, relief=FLAT )

var.set("Authors Value: Day=25, Night=15")
#label.pack()
label.place(x = 540,y = 40)

### caption (authors values light limit)
var = StringVar()
label = Label( top, textvariable=var, relief=FLAT )

var.set("Authors Value: Day=240, Night=650")
label.pack()
label.place(x = 540,y = 180)

### caption (radio buttons)
var = StringVar()
label = Label( top, textvariable=var, relief=FLAT )

var.set("Select  photo  resolution")
label.pack()
label.place(x = 10,y = 170)

### caption (day interval)
var_day = StringVar()
label = Message( top, textvariable = var_day, relief = FLAT, width = 100 )

var_day.set("Day  Photo Interval")
label.pack()
label.place(x = 540,y = 80)

### caption (night interval)
var_night = StringVar()
label = Message( top, textvariable = var_night, relief = FLAT, width = 100 )

var_night.set("Night Photo Interval")
label.pack()
label.place(x = 690,y = 80)

### caption (day light limit)
var_day = StringVar()
label = Message( top, textvariable = var_day, relief = FLAT, width = 100 )

var_day.set("Day  Photo Light Limit")
label.pack()
label.place(x = 540,y = 220)

### caption (night light limit)
var_night = StringVar()
label = Message( top, textvariable = var_night, relief = FLAT, width = 100 )

var_night.set("Night Photo  Light   Limit")
label.pack()
label.place(x = 690,y = 220)

### button 1
def open_readme():
    subprocess.call(['lxterminal', '-e', 'mousepad ../readme.txt'])

B1 = Button(top, text = "Open  'ReadMe'", command = open_readme, bg='dimgrey', fg='white')
B1.place(x = 10,y = 40)

### button 2
def view_configfile():
    subprocess.call(['lxterminal', '-e', 'mousepad cam_configfile.yaml'])

B2 = Button(top, text = "View  configfile", command = view_configfile, bg='dimgrey', fg='white')
B2.place(x = 10,y = 80)

### button 5
def preview():
    subprocess.call(['lxterminal', '-e', 'python3 cam_preview.py cam_configfile.yaml'])

B5 = Button(top, text = "Adjust  angle  (preview)", command = preview, bg='dimgrey', fg='white')
B5.place(x = 10,y = 120)

### button 3 (start camera)
def start_camera():
    subprocess.call(['lxterminal', '-e', 'python3 day-and-night-timelapse-full-v2.3.2.py cam_configfile.yaml'])

B3 = Button(top, text = "Start Camera", command = start_camera, bg='green', fg='white')
B3.place(x = 530,y = 480)

### button 4 (stop camera)
def stop_camera():
    subprocess.call(['lxterminal', '-e', 'kill $(ps aux | grep "day-and-night-timelapse-full-v2.3.2.py cam_configfile.yaml" && ps aux | grep "_mode.py" )'])
    subprocess.call(['lxterminal', '-e', 'kill $(ps aux | grep "_mode.py" )'])

B4 = Button(top, text = "Stop Camera", command = stop_camera, bg='red', fg='white')
B4.place(x = 660,y = 480)

### button 6 (start day mode)
def start_camera():
    subprocess.call(['lxterminal', '-e', 'python3 day_mode.py cam_configfile.yaml'])

B6 = Button(top, text = " Start Day Mode ", command = start_camera, bg='skyblue', fg='white')
B6.place(x = 235,y = 480)

### button 7 (start night mode)
def stop_camera():
    subprocess.call(['lxterminal', '-e', 'python3 night_mode.py cam_configfile.yaml'])

B7 = Button(top, text = "Start Night Mode", command = stop_camera, bg='navy', fg='white')
B7.place(x = 380,y = 480)

### radiobuttons (resolution)
def sel_resolution():
   selected_resolution = str(var.get())
   sel_resolution.selected = selected_resolution

root = top
var = StringVar()
var.set (current_resolution)

R1 = Radiobutton(root, text="2592x1944,   4:3,   FOV full,   binning none", variable=var, value='2592, 1944', command=sel_resolution)
R1.place(x = 10,y = 200)

R2 = Radiobutton(root, text="1920x1080,   16:9,   FOV partial,   binning none", variable=var, value='1920, 1080', command=sel_resolution)
R2.place(x = 10,y = 230)

R3 = Radiobutton(root, text="1296x730,   16:9,   FOV full,   binning 2x2 ", variable=var, value='1296, 730', command=sel_resolution)
R3.place(x = 10,y = 260)

R4 = Radiobutton(root, text="640x480,   4:3,   FOV full,   binning 4x4 ", variable=var, value='640, 480', command=sel_resolution)
R4.place(x = 10,y = 290)

### spinbox1 day light limit
def spbx1_day_light_limit():
   spbx1_selection_day = int(spbx1var.get())
   spbx1_day_light_limit.selectionn = spbx1_selection_day

spbx1var = IntVar()
spbx1var.set(current_day_light_limit)
spinbox_day = Spinbox( top, from_=1, to=1000, width=5, textvariable=spbx1var )
spinbox_day.place(x = 545,y = 260)

### spinbox2 night light limit
def spbx2_night_light_limit():
   spbx2_selection_night = int(spbx2var.get())
   spbx2_night_light_limit.selectionn = spbx2_selection_night

spbx2var = IntVar()
spbx2var.set(current_night_light_limit)
spinbox_night = Spinbox( top, from_=1, to=1000, width=5, textvariable=spbx2var )
spinbox_night.place(x = 695,y = 260)

### spinbox3 day interval
def select_interval_day():
   spbx3_selection_day = int(spbx3var.get())
   select_interval_day.selection = spbx3_selection_day

spbx3var = IntVar()
spbx3var.set(current_day_value_in_configfile)
spinbox_day_interval = Spinbox( top, from_=1, to=1000, width=5, textvariable=spbx3var )
spinbox_day_interval.place(x = 545,y = 120)

### spinbox4 night interval
def select_interval_night():
   spbx4_selection_night = int(spbx4var.get())
   select_interval_night.selection = spbx4_selection_night

spbx4var = IntVar()
spbx4var.set(current_night_value_in_configfile)
spinbox_night_interval = Spinbox( top, from_=1, to=1000, width=5, textvariable=spbx4var )
spinbox_night_interval.place(x = 695,y = 120)

### entry box1 (day photo destination)
def entrybox1():
    entrbx1 = str(e1_str.get())
    entrybox1.selection = entrbx1

my_w = top
l1 = Label(my_w,  text='Day Photo Destination:', width=20)  # added one Label
l1.place(x = 8, y = 330)

e1_str = StringVar()
e1_str.set(current_day_destination_path)
e1 = Entry(my_w,   width=70,bg='yellow', textvariable=e1_str) # added one Entry box
e1.place(x = 195, y = 330)


### entry box2 (night photo destination)
def entrybox2():
    entrbx2= str(e2_str.get())
    entrybox2.selection = entrbx2

my_w = top
l2 = Label(my_w,  text=' Night Photo Destination:', width=20 )  # added one Label
l2.place(x = 10, y = 370)

e2_str = StringVar()
e2 = Entry(my_w,   width=70,bg='yellow', textvariable=e2_str) # added one Entry box
e2.place(x = 195, y = 370)
e2_str.set(current_night_destination_path)

### entry box3 (ineligible files destination)
def entrybox3():
    entrbx3= str(e3_str.get())
    entrybox3.selection = entrbx3

my_w = top
l3 = Label(my_w,  text='Ineligible files Destination:', width=25 )  # added one Label
l3.place(x = 2, y = 410)

e3_str = StringVar()
e3 = Entry(my_w,   width=70,bg='yellow', textvariable=e3_str) # added one Entry box
e3.place(x = 195, y = 410)
e3_str.set(current_ineligible_files_path)

### apply button
def apply_button():
    select_interval_day()
    select_interval_night()
    sel_resolution()
    spbx1_day_light_limit()
    spbx2_night_light_limit()
    entrybox1()
    entrybox2()
    entrybox3()
    with open(fname, "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
        cfg['day_config']['dinterval'] = select_interval_day.selection
        cfg['night_config']['ninterval'] = select_interval_night.selection
        cfg['camera_parameters']['resolution'] = sel_resolution.selected
        cfg['day_config']['dlight_low_limit'] = spbx1_day_light_limit.selectionn
        cfg['night_config']['nlight_low_limit'] = spbx2_night_light_limit.selectionn
        cfg['path_vars']['ddest_photo_day'] = entrybox1.selection
        cfg['path_vars']['ndest_photo_night'] = entrybox2.selection
        cfg['path_vars']['ineligible_files'] = entrybox3.selection
    with open(fname, 'w') as outfile:
        yaml.dump(cfg, outfile, default_flow_style=False, sort_keys=False)

B4 = Button(top, text = "Apply and save to configfile", command = apply_button, bg='orange', fg='white')
B4.place(x = 10,y = 480)


label = Label(root)
label.pack()

### end
top.mainloop()
