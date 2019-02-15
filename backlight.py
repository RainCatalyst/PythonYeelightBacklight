'''
Config
---------
The lamp ip adress (look in the router)
'''
LAMP_IP = '192.168.1.46'
'''
Minimum color delta to change lamp color (decreasing this value increases flashing)
'''
THRESHOLD = 0.6
'''
Minimum number of frames between color changes (decreasing this value increases flashing, smaller numbers better for action films)
'''
MIN_CHANGE_FRAMES = 80
'''
The time of lerping one color to another (smaller numbers better for action films)
'''
DURATION = 650
'''
Interval between screen captures
'''
UPDATEINTERVAL = 0.1
'''
Get color of each DECIMATE pixel
(Increasing this value allows better average color calculation at cost of increased cpu usage)
'''
DECIMATE = 8

print('Starting')

from yeelight.transitions import *
from yeelight import Flow, Bulb
import keyboard
import matplotlib.pyplot as plt

bulb = Bulb(LAMP_IP, effect='smooth', duration=DURATION)
bulb.start_music()

from PIL import ImageGrab
import time
import os
import colorsys

image = ImageGrab.grab()
width = image.size[0]
height = image.size[1]
rescale = (height*width)/(DECIMATE**2)

old_hsv = [0,0,0]
total_threshold = 0
total_changes = 0
change_frames = 0
total_change_frames = 0
deltas = []
count = 0

print('Image dimensions X:', width, 'Y:', height, '\nWorking...')

while True:
        #Exit if q is pressed
        if keyboard.is_pressed('q'):
                break

        #Make a screenshot and calculate average color
        image = ImageGrab.grab()
        image = image.load()
        red, green, blue = 0, 0, 0
        for y in range(0, height, DECIMATE):
                for x in range(0, width, DECIMATE):
                        color = image[x, y]
                        red += color[0]
                        green += color[1]
                        blue += color[2]
        red /= rescale
        green /= rescale
        blue /= rescale
        h = colorsys.rgb_to_hsv(red/255, green/255, blue/255)
        #Calculate color delta
        delta = abs(h[0]-old_hsv[0])+abs(h[1]-old_hsv[1])+abs(h[2]-old_hsv[2])
        #Change the lamp color if all conditions are met
        if delta > THRESHOLD and change_frames>MIN_CHANGE_FRAMES:
                total_changes += 1
                try:
                        bulb.set_hsv(int(h[0] * 360), int(h[1] * 100), int(h[2] * 25))
                        #TODO: Set brightness (for some reason it doesnt work)
                except Exception as e:
                        print(e)
                old_hsv = h
                total_change_frames += change_frames
                change_frames = 0
        change_frames += count
        count+=1
        time.sleep(UPDATEINTERVAL)
#bulb.stop_music() Gives error
print('Stopped')
