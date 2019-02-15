# PythonYeelightBacklight
Backlight python script for Xiaomi Yeelight

# How to setup
1. Install python
2. Install dependencies (pip install yeelight, keyboard, Pillow)
3. Change your lamp ip in script config (inside script)
4. Configure other params (*optional*)
4. Run it

# Best parameters
I havent configured best config params yet so feel free to experiment. Default params are average for any type of films.
Decrease threshold and duration for action films with a lot of screen changes.
Increase threshold and duration for films with less screen changes.
MIN_CHANGE_FRAMES is usually ok, you can make it bigger if you are experiencing troubles with the lamp.

I did a small research for  [Apex Legends Trailer](https://www.youtube.com/watch?v=BSd7lg9Imzo) to make the config values better.
Here is what I got

```
Total time 60.7 seconds 1.0 minutes
Frame count 607
Total Threshold 177.3
Total Changes 54
Average Changes per minute 53.4
Average Threshold 0.29
Average frames between changes 78.2
```
Color delta values graph (x = frames)
![Color delta](https://raw.githubusercontent.com/RainCatalyst/PythonYeelightBacklight/master/deltas.png)

So I created a few configs that work quite well

1. Relaxing
```
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
MIN_CHANGE_FRAMES = 300
'''
The time of lerping one color to another (smaller numbers better for action films)
'''
DURATION = 1000
'''
Interval between screen captures
'''
UPDATEINTERVAL = 0.15
'''
Get color of each DECIMATE pixel
(Increasing this value allows better average color calculation at cost of increased cpu usage)
'''
DECIMATE = 8
```
2. Action
```
'''
Config
---------
The lamp ip adress (look in the router)
'''
LAMP_IP = '192.168.1.46'
'''
Minimum color delta to change lamp color (decreasing this value increases flashing)
'''
THRESHOLD = 0.5
'''
Minimum number of frames between color changes (decreasing this value increases flashing, smaller numbers better for action films)
'''
MIN_CHANGE_FRAMES = 80
'''
The time of lerping one color to another (smaller numbers better for action films)
'''
DURATION = 600
'''
Interval between screen captures
'''
UPDATEINTERVAL = 0.1
'''
Get color of each DECIMATE pixel
(Increasing this value allows better average color calculation at cost of increased cpu usage)
'''
DECIMATE = 8
```
# TODO
- Change lamp brightness for more contrast
- Do more research with different films to find the best parameters
- Deal with lamp socket errors (*if possible*)
