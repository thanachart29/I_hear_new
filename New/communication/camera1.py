from curses import raw
import platform
from numpy import clip
import serial
import time
import sys
import cv2
import os

raw_folder_path = 'New/communication/rawdata3'
frame_list = []
count = len(os.listdir(raw_folder_path + '/bottom'))-1

print(count)

for j in range(4):
    count += 1
    print("!!Open Top LED!!")
    time.sleep(0.1)
    camera = cv2.VideoCapture(0)
    time.sleep(0.9)
    ret, frame = camera.read()
    if(ret == True):
        cv2.imwrite((raw_folder_path + '/bottom/bottom_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame)
        print("!!Image Saved!!")
        print("Count : " + str(len(os.listdir(raw_folder_path + '/bottom'))-1))
    print("!!Open Side LED!!")
    time.sleep(0.1)
    camera = cv2.VideoCapture(0)
    time.sleep(0.9)
    ret, frame = camera.read()
    if(ret == True):
        cv2.imwrite((raw_folder_path + '/side/side_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame)
        print("!!Image Saved!!")
        print("Count : " + str(len(os.listdir(raw_folder_path + '/side'))-1))
    print("!!Open Stick LED!!")
    time.sleep(0.1)
    camera = cv2.VideoCapture(0)
    time.sleep(0.9)
    ret, frame = camera.read()
    if(ret == True):
        cv2.imwrite((raw_folder_path + '/stick/stick_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame)
        print("!!Image Saved!!")
        print("Count : " + str(len(os.listdir(raw_folder_path + '/stick'))-1))
    if j < 3:
        print("!!Drive Motor about 90 Degree!!")
        time.sleep(2)

count = 0
print("!!Open Side LED!!")
time.sleep(0.1)
camera = cv2.VideoCapture(0)
time.sleep(0.9)
startTime = time.time()*1000
clip_path = (raw_folder_path + '/clip/clip' + str(len(os.listdir(raw_folder_path + '/clip'))))
os.mkdir(clip_path)
while((time.time()*1000 - startTime) < 8150):
    count += 1
    ret, frame = camera.read()
    if(ret == True):
        cv2.imwrite((clip_path + '/img_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame)
        print("!!Image Saved!!")