import cv2
import numpy as np
import time
from PIL import ImageGrab

def processImg(img):
    original_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    low_green = np.array([40,40,40])
    high_green = np.array([70, 255,255])
    mask = cv2.inRange(original_img,low_green,high_green)
    new_mask = cv2.bitwise_and(img,img,mask=mask)
    return new_mask

last_time = time.time()
while True:
    printScreen = np.array(ImageGrab.grab(bbox=(85,740,400,905)))
    new_screen = processImg(printScreen)
    contours,hierachy = cv2.findContours(new_screen,1,cv2.CHAIN_APPROX_NONE)

##    numpyScreen = np.array(printScreen.getdata(),dtype='uint8')
    print("Loop took {} seconds".format(time.time() - last_time))
    last_time = time.time()
    cv2.imshow('mask',new_screen)
##    cv2.imshow('window',np.array(printScreen))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break