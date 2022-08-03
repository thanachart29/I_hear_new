import platform
import serial
import time
import sys
import cv2
import os as pyOS

raw_folder_path = 'rawdata3'
frame_list = []
count = 0

def serialWait(self):
    while(ser.in_waiting == 0):
        pass

os = platform.platform()[0].upper()
if os == 'M': #Mac
    ser = serial.Serial('/dev/cu.usbmodem1103', 115200, parity='E', stopbits=1, timeout=1)
elif os == 'W': #Windows
    ser = serial.Serial('COM10',115200,parity='E',stopbits=1,timeout=1)

time.sleep(2)

for j in range(4):
    count += 1
    for i in range(167,170,2):
        buffer = [178, i]
        ser.write(buffer)
        serialWait()
        serialRead = bytearray(ser.read(2))
        if (serialRead[0] == 178):
            if (serialRead[1] == 168):
                camera = cv2.VideoCapture(0)
                ret, frame = camera.read()
                if(ret == True):
                    cv2.imwrite(raw_folder_path + '/bottom/bottom_' + str(('0'*(4-len(count))) + str(count)) + '.jpg')
            elif (serialRead[1] == 170):
                camera = cv2.VideoCapture(0)
                ret, frame = camera.read()
                if(ret == True):
                    cv2.imwrite(raw_folder_path + '/side/side_' + str(('0'*(4-len(count))) + str(count)) + '.jpg')

    buffer = [178, 167]
    ser.write(buffer)
    serialWait()
    serialRead = bytearray(ser.read(2))
    if (serialRead[0] == 178):
        if (serialRead[1] == 168):
            camera = cv2.VideoCapture(0)
            ret, frame = camera.read()
            if(ret == True):
                cv2.imwrite(raw_folder_path + '/stick/stick_' + str(('0'*(4-len(count))) + str(count)) + '.jpg')

buffer = [178, 167]
ser.write(buffer)
serialWait()
serialRead = bytearray(ser.read(2))
if (serialRead[0] == 178):
    if (serialRead[1] == 168):
        camera = cv2.VideoCapture(0)
        startTime = time.time()*1000
        while((time.time()*1000 - startTime) < 8150):
            count += 1
            ret, frame = camera.read()
            if(ret == True):
                cv2.imwrite(raw_folder_path + '/clip/clip' + str(len(pyOS.listdir(raw_folder_path + '/clip'))+1) + '/img_' + str(('0'*(4-len(count))) + str(count)) + '.jpg')