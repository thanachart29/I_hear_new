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
count = 24
input = 0
camera1 = cv2.VideoCapture(input)   #Top camera
# camera2 = cv2.VideoCapture(3)   #Side camera
# camera3 = cv2.VideoCapture(1)   #Bottom camera1
# camera4 = cv2.VideoCapture(0)   #Bottom camera2

if (input == 1 or input == 0):
    camera1.set(3, 1280)
    camera1.set(4, 720)
time.sleep(2)
ret, frame = camera1.read()
if(ret == True and input == 3):
    cv2.imwrite((raw_folder_path + '/side/side_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame)
if(ret == True and input == 1):
    cv2.imwrite((raw_folder_path + '/stick/frame1/stick_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame)
if(ret == True and input == 0):
    cv2.imwrite((raw_folder_path + '/stick/frame2/stick_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame)
print('finished')
# clip_path = (raw_folder_path + '/clip/clip' + str(len(os.listdir(raw_folder_path + '/clip'))))
# os.mkdir(clip_path)
# while((time.time()*1000 - startTime) < 8150):
#     count += 1
#     ret4, frame4 = camera2.read()
#     if(ret4 == True):
#         cv2.imwrite((clip_path + '/img_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame4)
#         print("!!Image Saved!!")

# camera3.set(3, 1280)
# camera3.set(4, 720)
# camera4.set(3, 1280)
# camera4.set(4, 720)
# time.sleep(2)

# print(count)

# for j in range(4):
#     count += 1
#     # print("!!Open Top LED!!")
#     # time.sleep(0.9)
#     # ret, frame = camera1.read()
#     # if(ret == True):
#     #     cv2.imwrite((raw_folder_path + '/bottom/bottom_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame)
#     #     print("!!Image Saved!!")
#     #     print("Count : " + str(len(os.listdir(raw_folder_path + '/bottom'))-1))
#     print("!!Open Stick LED!!")
#     time.sleep(2)
#     ret2, frame2 = camera3.read()
#     if(ret2 == True):
#         cv2.imwrite((raw_folder_path + '/stick/frame1/stick_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame2)
#         print("!!Image Saved!!")
#         print("Count : " + str(len(os.listdir(raw_folder_path + '/stick'))-1))
#     time.sleep(2)
#     ret3, frame3 = camera4.read()
#     cv2.waitKey(100)
#     if(ret3 == True):
#         cv2.imwrite((raw_folder_path + '/stick/frame2/stick1_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame3)
#         print("!!Image Saved!!")
#         print("Count : " + str(len(os.listdir(raw_folder_path + '/stick'))-1))
#     print("!!Open Side LED!!")
#     time.sleep(2)
#     ret1, frame1 = camera2.read()
#     if(ret1 == True):
#         cv2.imwrite((raw_folder_path + '/side/side_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame1)
#         print("!!Image Saved!!")
#         print("Count : " + str(len(os.listdir(raw_folder_path + '/side'))-1))
#     if j < 3:
#         print("!!Drive Motor about 90 Degree!!")
#         time.sleep(4)

# count = 0
# print("!!Open Side LED!!")
# time.sleep(0.9)
# startTime = time.time()*1000
# clip_path = (raw_folder_path + '/clip/clip' + str(len(os.listdir(raw_folder_path + '/clip'))))
# os.mkdir(clip_path)
# while((time.time()*1000 - startTime) < 8150):
#     count += 1
#     ret4, frame4 = camera2.read()
#     if(ret4 == True):
#         cv2.imwrite((clip_path + '/img_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame4)
#         print("!!Image Saved!!")