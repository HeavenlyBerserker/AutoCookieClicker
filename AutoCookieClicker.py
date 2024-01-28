
import pyautogui
import cv2
import numpy as np

from pynput import keyboard
from pynput.mouse import Button, Controller

import time
import datetime

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

# Upgrades column
upgrades = []
for y in range(30,1033, int(1000/16)):
    upgrades.append((1689,y))
upgrades.append((1689,1029))

# Params
innercounter = 500 # approx 10s for 500
cooldown = 0.00001
screen = 2
# Upgrade params
upgrades_buy = True
research_interval = 15*12 # Depends on innercounter
# Building params
building_buy = False
# Spells params
autospell = True
spell_interval = 180

pynput_mouse = Controller()

pyautogui.press('f6')

# Move to second screen
offset = 0
if(screen == 2):
    offset = 1920
    
    newcoors = []
    for coor in coors:
        newcoors.append((coor[0]-offset, coor[1]))
    coors = newcoors

    newupgrades = []
    for coor in upgrades:
        newupgrades.append((coor[0]-offset, coor[1]))
    upgrades = newupgrades

counter = 0

starting = time.time()

while(True):

    # Auto-upgrader
    if(upgrades_buy and counter%research_interval == 0):
        pyautogui.press('f6')
        pynput_mouse.position = (1626-offset, 167)
        pynput_mouse.scroll(0, 6)
        time.sleep(1)
        pynput_mouse.click(Button.left)
        time.sleep(1)
        pynput_mouse.position = (1626-offset, 167)
        pynput_mouse.scroll(0, -4)
        time.sleep(0.5)
        pyautogui.press('f6')

    if(autospell and counter%spell_interval == 0):
        pyautogui.press('f6')
        # Auto cast spell
        pynput_mouse.position = (1458-offset, 314)# View Grimoire
        mouse.click()
        time.sleep(0.5)
        pynput_mouse.position = (901-offset, 232)# Golden cookie spell
        mouse.click()
        pynput_mouse.position = (1421-offset, 333)# Close Grimoire
        mouse.click()
        time.sleep(0.5)
        pyautogui.press('f6')

    # Golden Cookie Hunt
    for coor in coors:
        mouse.move(coor[0], coor[1], absolute=True)
        mouse.click()

    # Cookie click
    mouse.move(314-offset, 409, absolute=True)
    for i in range(innercounter):
        mouse.click()
        time.sleep(cooldown)

    # Grandmapocalipse
    #mouse.move(1615, 120, absolute=True)
    #mouse.click()

    # Building auto buyer
    # Logarithmic
    if(building_buy):
        ratio = 2
        start = 14
        r = random.randint(int((start)**ratio), int((len(upgrades)-1)**ratio))
        r = int(r**(1/ratio))
        # Uniform
        # r = random.randint(0, len(upgrades)-1)
        #Clicking
        mouse.move(upgrades[r][0], upgrades[r][1], absolute=True)
        mouse.click()

    # The event listener will be running in this block
    with keyboard.Events() as events:
        # Block at most twenieth of a second
        event = events.get(0.05)
        if event is None:
            counter += 1
        else:
            if(event.key == keyboard.Key.esc):
                print("Executed", counter, "cycles.")
                print(counter* innercounter, "cookie clicks.")
                ending = time.time()
                print(str(datetime.timedelta(seconds=ending-starting)), "elapsed.")
                sys.exit("Exited")

print("------------------------------------")

