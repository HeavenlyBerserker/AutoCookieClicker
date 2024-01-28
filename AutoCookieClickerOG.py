
import pyautogui
import cv2
import numpy as np

import time

import random

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
x0 =616
xf =853
y0 =149
for x in range(x0,xf,interval):
    coors.append((x,y0))
x0 =1359
xf =1578
y0 =149
for x in range(x0,xf,interval):
    coors.append((x,y0))
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
y0 =125
for x in range(x0,xf,interval):
    coors.append((x,y0))
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

coors.append((-405,572))

upgrades = []

for y in range(30,1033, int(1000/16)):
    upgrades.append((1612,y))

#mouse = Controller()

'''
while(True):
    for coor in coors:
        pyautogui.click(coor[0], coor[1])
'''

counter = 10
innercounter = 2000
thresh = 0.5

picmax = 4

imgs0 = []
imgs = []

for i in range(picmax):
    img = cv2.imread("Picture"+str(i)+".png")
    imgs0.append(img)
    imgs.append(img)

for img in imgs0:
    imgs.append(cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE))
    imgs.append(cv2.rotate(img, cv2.ROTATE_180))
    imgs.append(cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE))

print(len(imgs))

i = 0
for im in imgs:
    fn = "deb/"+str(i)+".png"
    cv2.imwrite(fn,im)
    i += 1

pyautogui.press('f6')

while(True):

    #cap = np.array(pyautogui.screenshot())

    '''
    i = 0
    for template in imgs:
        res = cv2.matchTemplate(cap,template,3)
        
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        h, w, c = template.shape
        im = cap[max_loc[0]:max_loc[0]+h, max_loc[1]:max_loc[1]+w, :]
        if(im.shape[0] > 0 and im.shape[1] > 0):
            fn = "deb/match"+str(i)+ "_" + str(max_val) + ".png"
            cv2.imwrite(fn,im)
        print(max_val)
        
        
        if((max_loc[1] > 21 and max_loc[1] < 1033 and max_loc[0] < 576)
           or (max_loc[1] < 1033 and max_loc[1] > 181 and max_loc[0] > 576 and max_loc[0] < 1590)
           or (max_loc[0] > 698 and max_loc[0] < 1477 and max_loc[1] > 24 and max_loc[1] < 102)):
            if(max_val > thresh):
                pyautogui.click(max_loc[0], max_loc[1])
        i += 1
    

    mouse.position = (294, 420)
    for i in range(innercounter):
        mouse.click(Button.left)
        #pyautogui.click(294, 420)

    for coor in coors:
        mouse.position = (coor[0], coor[1])
        mouse.click(Button.left)
        #pyautogui.click(coor[0], coor[1])
    '''

    '''
    mouse.move(294, 420, absolute=True)
    for i in range(innercounter):
        mouse.click()
        #pyautogui.click(294, 420)
    '''
    '''
    pyautogui.press('f6')
    mouse.move(1631, 162, absolute=True) # buy
    mouse.click()
    mouse.move(1806, 172, absolute=True) # 100
    mouse.click()
    time.sleep(0.001)
    mouse.move(1767, 211, absolute=True) # Cursor
    mouse.click()
    time.sleep(0.001)
    mouse.move(1628, 182, absolute=True) # Sell
    mouse.click()
    pyautogui.press('f6')
    time.sleep(2.5)
    mouse.move(1869, 176, absolute=True) # All
    mouse.click()
    mouse.move(1767, 211, absolute=True) # Cursor
    mouse.click()
    mouse.move(1690, 167, absolute=True) # 1
    mouse.click()
    '''
    
    for coor in coors:
        mouse.move(coor[0], coor[1], absolute=True)
        #time.sleep(0.0001)
        mouse.click()
        #pyautogui.click(coor[0], coor[1])

    #ratio = 1.5    
    #r = random.randint(0, int((len(upgrades)-1)**ratio))
    #r = int(r**(1/ratio))

    #r = random.randint(14, len(upgrades)-1)

    #mouse.move(upgrades[r][0], upgrades[r][1], absolute=True)

    #Grandmapocalipse
    #mouse.move(1615, 120, absolute=True)
    #mouse.click()

    time.sleep(7.5)

    #cv2.imwrite("cap.png",cap)
    #print(cap.shape)

    counter -= 1

print("------------------------------------")

