import platform
import serial
import time
import cv2
import os

raw_folder_path = 'rawData4'
frame_list = []
count = 0
top_camera = cv2.VideoCapture(0)
while not(top_camera.isOpened()):
    pass
side_camera = cv2.VideoCapture(1)
while not(side_camera.isOpened()):
    pass
bottom_camera1 = cv2.VideoCapture(2)
while not(bottom_camera1.isOpened()):
    pass
bottom_camera2 = cv2.VideoCapture(3)
while not(bottom_camera2.isOpened()):
    pass
print('All CAM Ready!!')

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
    for i in range(167,172,2):
        buffer = [178, i]
        ser.write(buffer)
        serialWait()
        serialRead = bytearray(ser.read(2))
        if (serialRead[0] == 178):
            if (serialRead[1] == 168):
                ret, frame = top_camera.read()
                if(ret == True):
                    cv2.imwrite(raw_folder_path + '/bottom/bottom_' + str(('0'*(4-len(count))) + str(count)) + '.jpg')
                    print('!!Bottom_Image saved!!')
            elif (serialRead[1] == 170):
                ret, frame = side_camera.read()
                if(ret == True):
                    cv2.imwrite(raw_folder_path + '/side/side_' + str(('0'*(4-len(count))) + str(count)) + '.jpg')
                    print('!!Side_Image saved!!')
            elif (serialRead[1] == 172):
                ret, frame = bottom_camera1.read()
                if(ret == True):
                    cv2.imwrite(raw_folder_path + '/stick/frame1/stick_' + str(('0'*(4-len(count))) + str(count)) + '.jpg')
                    print('!!Stick_Image_frame1 saved!!')
                ret, frame = bottom_camera2.read()
                if(ret == True):
                    cv2.imwrite(raw_folder_path + '/stick/frame2/stick_' + str(('0'*(4-len(count))) + str(count)) + '.jpg')
                    print('!!Stick_Image_frame2 saved!!')

buffer = [178, 169]
ser.write(buffer)
serialWait()
serialRead = bytearray(ser.read(2))
if (serialRead[0] == 178):
    if (serialRead[1] == 170):
        startTime = time.time()*1000
        while((time.time()*1000 - startTime) < 10150):
            count += 1
            ret, frame = side_camera.read()
            if(ret == True):
                cv2.imwrite(raw_folder_path + '/clip/clip' + str(len(os.listdir(raw_folder_path + '/clip'))+1) + '/img_' + str(('0'*(4-len(count))) + str(count)) + '.jpg')
                print('!!Frame[' + str(count) + '] saved!!')
side_camera.release()
top_camera.release()
bottom_camera1.release()
bottom_camera2.release()