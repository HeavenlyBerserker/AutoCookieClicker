
import pyautogui
import cv2
import numpy as np

from pynput import keyboard

import time

import random

import sys

#from pynput import mouse
#from pynput.mouse import Controller, Button
import mouse

interval = 50
intervalgrid = 60

coors = []

# Corner cases
coors.append((585,58))
coors.append((587,103))
coors.append((693,68))
coors.append((1485,65))
coors.append((584,163))

# Around name
x0 =71
xf =493
y0 =85
for x in range(x0,xf,interval):
    coors.append((x,y0))
x0 =71
xf =493
y0 =119
for x in range(x0,xf,interval):
    coors.append((x,y0))

# Building band left
x0 =616
xf =825
y0 =149
for x in range(x0,xf,interval):
    coors.append((x,y0))

# Building band right
x0 =1381
xf =1578
y0 =149
for x in range(x0,xf,interval):
    coors.append((x,y0))

# Text band 3 strips
x0 =694
xf =1483
y0 =44
for x in range(x0,xf,interval):
    coors.append((x,y0))
x0 =694
xf =1483
y0 =75
for x in range(x0,xf,interval):
    coors.append((x,y0))
x0 =694
xf =1414
y0 =131
for x in range(x0,xf,interval):
    coors.append((x,y0))

# Building band below
x0 =862
xf =1338
y0 =175
for x in range(x0,xf,interval):
    coors.append((x,y0))

#Grid
for x in range(0,1590,intervalgrid):
    if(x%2 == 1):
        yoffset = int(intervalgrid/2)
    else:
        yoffset = 0
    for y in range(yoffset,1033,intervalgrid):
        if((y > 21 and y < 1033 and x < 576 and not (x > 68 and y > 81 and x < 508 and y < 113) and not (x > 0 and y > 930 and x < 60 and y < 1050))
               or (y < 1033 and y > 181 and x > 576 and x < 1590)):
            coors.append((x,y))

coors.append((-53,572))

upgrades = []

for y in range(30,1033, int(1000/16)):
    upgrades.append((1612,y))

counter = 10
innercounter = 500 # approx 10s for 500
cooldown = 0.00001

#pyautogui.press('f6')

while(True):

    # Golden Cookie Hunt
    for coor in coors:
        mouse.move(coor[0], coor[1], absolute=True)
        mouse.click()

    # Cookie click
    mouse.move(314, 409, absolute=True)
    for i in range(innercounter):
        mouse.click()
        time.sleep(cooldown)

    # Building auto buyer
    #ratio = 1.5    
    #r = random.randint(0, int((len(upgrades)-1)**ratio))
    #r = int(r**(1/ratio))

    #r = random.randint(14, len(upgrades)-1)

    #mouse.move(upgrades[r][0], upgrades[r][1], absolute=True)

    # Grandmapocalipse
    #mouse.move(1615, 120, absolute=True)
    #mouse.click()

    # The event listener will be running in this block
    with keyboard.Events() as events:
        # Block at most one second
        event = events.get(0.05)
        if event is None:
            counter -= 1
        else:
            if(event.key == keyboard.Key.esc):
                sys.exit("Exited")

print("------------------------------------")

