import cv2
import numpy as np

def prr(x):
    print(x)
    
def Rotate(src, degrees):
    if degrees == 90:
        dst = cv2.transpose(src) 
        dst = cv2.flip(dst, 1)   

    elif degrees == 180:
        dst = cv2.flip(src, 0)   

    elif degrees == 270:
        dst = cv2.transpose(src)
        dst = cv2.flip(dst, 0)  
    else:
        dst = null
    return dst

def green(frame):
    frameprime = frame.copy()
    for items in frameprime:
        for item in items:
            item[0] = 0;
            item[2] = 0;
    return frameprime

def blue(frame):
    frameprime = frame.copy()
    for items in frameprime:
        for item in items:
            item[1] = 0;
            item[2] = 0;
    return frameprime

def red(frame):
    frameprime = frame.copy()
    for items in frameprime:
        for item in items:
            item[0] = 0;
            item[1] = 0;
    return frameprime

def zero(frame):
    frameprime = frame.copy()
    for items in frameprime:
        for item in items:
            item[0] = 0;
            item[1] = 0;
            item[2] = 0;
    return frameprime

def edge(frame):
    
    frameprime = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)

    #http://docs.opencv.org/trunk/d4/d73/tutorial_py_contours_begin.html
    ret, thresh = cv2.threshold(frameprime, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(im2, contours, -1, (0,255,0), 3)
    #frame.tolist()

    frameprime = zero(frame)
    cv2.drawContours(frameprime, contours, -1, (255,0,0), 3)
    return frameprime
