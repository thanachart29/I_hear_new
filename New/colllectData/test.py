import platform
import serial
import time
import cv2
import os

def serialWait():
    while(ser.in_waiting == 0):
        pass

osys = platform.platform()[0].upper()
if osys == 'M': #Mac
    ser = serial.Serial('/dev/cu.usbmodem1201', 9600, stopbits=1, timeout=1)
elif osys == 'W': #Windows
    ser = serial.Serial('COM10',115200,parity='E',stopbits=1,timeout=1)
time.sleep(2)

for i in range(5):

    buffer = [104]
    ser.write(buffer)
    # serialWait()
    # print(ser.read(12))
    time.sleep(3)
