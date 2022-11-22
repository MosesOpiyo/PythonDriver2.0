import cv2
import numpy as np
import time
from PIL import ImageGrab

from directkeys import PressKey,ReleaseKey,W,S,D,A

def Straight():
    PressKey(W)
    time.sleep(0.5)
    ReleaseKey(W)
    print("Straight")

def slightRight():
    PressKey(D)
    time.sleep(.5)
    ReleaseKey(D)
    print("slight right")

def slightLeft():
    PressKey(A)
    time.sleep(.5)
    ReleaseKey(A)
    print("slight left")

def Right():
    PressKey(D)
    time.sleep(2)
    ReleaseKey(D)
    print("right")

def Left():
    PressKey(A)
    time.sleep(2)
    ReleaseKey(A)
    print("left")

def sharpRight():
    PressKey(D)
    time.sleep(1)
    ReleaseKey(D)
    print("sharp right")

def sharpLeft():
    PressKey(A)
    
    time.sleep(1)
    ReleaseKey(A)
    print("sharp left")

def processImg(img):
    blurred_img = cv2.GaussianBlur(img, (5,5), 0)
    original_img = cv2.cvtColor(blurred_img,cv2.COLOR_BGR2HSV)
    low_green = np.array([40,40,40])
    high_green = np.array([70, 255,255])
    mask = cv2.inRange(original_img,low_green,high_green)
    new_mask = cv2.Canny(mask,50,150)
    return new_mask

last_time = time.time()
while True:
    printScreen = np.array(ImageGrab.grab(bbox=(150,740,315,845)))
    new_screen = processImg(printScreen)
    contours,hierachy = cv2.findContours(new_screen,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    if len(contours) > 0:
        c = max(contours,key = cv2.contourArea)
        M = cv2.moments(c)
        if M['m00'] != 0:
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            if cx >= 80 and cx <= 84:
                Straight()
            elif cx < 80:
                slightLeft()
                Straight()
            elif cx > 84:
                slightRight()
                Straight()
            print(f"CX: {cx} CY: {cy}")
    cv2.drawContours(printScreen, contours, -1, (0, 255,0), 2)
    last_time = time.time()
    cv2.imshow('window',printScreen)
##    cv2.imshow('window',np.array(printScreen))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break