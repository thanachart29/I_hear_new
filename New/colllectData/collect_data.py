import platform
import serial
import time
import cv2
import os

raw_folder_path = 'rawData4'
frame_list = []
count = 0
top_camera = 0
side_camera = 1
bottom_camera1 = 2
bottom_camera2 = 3

def serialWait(self):
    while(ser.in_waiting == 0):
        pass

osys = platform.platform()[0].upper()
if osys == 'M': #Mac
    ser = serial.Serial('/dev/cu.usbmodem1103', 115200, parity='E', stopbits=1, timeout=1)
elif osys == 'W': #Windows
    ser = serial.Serial('COM10',115200,parity='E',stopbits=1,timeout=1)
time.sleep(2)

count = len(os.listdir(raw_folder_path + '/side'))-1
print('Number of Durian : ' + str(int(count/4)))

for j in range(4):
    print('Angle[' + str(j+1) + ']')
    count += 1
    buffer = [10]
    ser.write(buffer)
    serialWait()
    serialRead = bytearray(ser.read(1))
    if (serialRead[0] == 10):
        camera = cv2.VideoCapture(top_camera)
        while not(camera.isOpened()):
            pass
        time.sleep(1)
        ret, frame = camera.read()
        if(ret == True):
            cv2.imwrite(raw_folder_path + '/bottom/bottom_' + str(('0'*(4-len(count))) + str(count)) + '.jpg')
            print('!!Bottom_Image saved!!')
            camera.release()
    buffer = [10]
    ser.write(buffer)
    serialWait()
    serialRead = bytearray(ser.read(1))
    if (serialRead[0] == 9):
        camera = cv2.VideoCapture(side_camera)
        while not(camera.isOpened()):
            pass
        time.sleep(1)
        ret, frame = camera.read()
        if(ret == True):
            cv2.imwrite(raw_folder_path + '/side/side_' + str(('0'*(4-len(count))) + str(count)) + '.jpg')
            print('!!Side_Image saved!!')
            camera.release()
    buffer = [10]
    ser.write(buffer)
    serialWait()
    serialRead = bytearray(ser.read(1))
    if (serialRead[0] == 9):
        camera = cv2.VideoCapture(bottom_camera1)
        while not(camera.isOpened()):
            pass
        time.sleep(1)
        ret, frame = camera.read()
        if(ret == True):
            cv2.imwrite(raw_folder_path + '/stick/frame1/stick_' + str(('0'*(4-len(count))) + str(count)) + '.jpg')
            print('!!Stick_Image_frame1 saved!!')
            camera.release()
        camera = cv2.VideoCapture(bottom_camera2)
        while not(camera.isOpened()):
            pass
        time.sleep(1)
        ret, frame = camera.read()
        if(ret == True):
            cv2.imwrite(raw_folder_path + '/stick/frame2/stick_' + str(('0'*(4-len(count))) + str(count)) + '.jpg')
            print('!!Stick_Image_frame2 saved!!')
            camera.release()
    buffer = [104]
    ser.write(buffer)
    serialWait()
    serialRead = bytearray(ser.read(1))
    if serialRead != 103:
        print('Communication Error!!!')
        break

buffer = [10]
ser.write(buffer)
serialWait()
serialRead = bytearray(ser.read(1))
buffer = [10]
ser.write(buffer)
serialWait()
serialRead = bytearray(ser.read(1))
if (serialRead[0] == 10):
    camera = cv2.VideoCapture(side_camera)
    while not(camera.isOpened()):
        pass
    time.sleep(1)
    startTime = time.time()*1000
    while((time.time()*1000 - startTime) < 10150):
        count += 1
        ret, frame = camera.read()
        if(ret == True):
            cv2.imwrite(raw_folder_path + '/clip/clip' + str(len(os.listdir(raw_folder_path + '/clip'))+1) + '/img_' + str(('0'*(4-len(count))) + str(count)) + '.jpg')
    camera.release()