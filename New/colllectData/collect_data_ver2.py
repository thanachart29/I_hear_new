import platform
import serial
import time
import cv2
import os

raw_folder_path = 'rawData4'
frame_list = []
count = len(os.listdir(raw_folder_path + '/side')) - 1

print('Count : ' + str(count))

def serialWait():
    while(ser.in_waiting == 0):
        pass

osys = platform.platform()[0].upper()
if osys == 'M': #Mac
    ser = serial.Serial('/dev/cu.usbmodem1201', 115200, parity='E', stopbits=1, timeout=1)
elif osys == 'W': #Windows
    ser = serial.Serial('COM10',115200,parity='E',stopbits=1,timeout=1)
time.sleep(2)

for i in range(4):
    count += 1
    buffer = [10] #BOTTOM LED
    ser.write(buffer)
    print('Open Bottom LED')
    bottom_camera1 = cv2.VideoCapture(1)
    bottom_camera2 = cv2.VideoCapture(3)
    bottom_camera1.set(3, 1280)
    bottom_camera1.set(4, 720)
    bottom_camera2.set(3, 1280)
    bottom_camera2.set(4, 720)
    time.sleep(1)
    ret, frame = bottom_camera1.read()
    ret1, frame1 = bottom_camera1.read()
    if(ret == True):
        cv2.imwrite((raw_folder_path + '/stick/frame1/stick_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame)
        print('!!Stick_Image_frame1 saved!!')
    else:
        print('Failed to read Stick_Image_frame1')
    if(ret1 == True):
        cv2.imwrite((raw_folder_path + '/stick/frame2/stick_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame1)
        print('!!Stick_Image_frame2 saved!!')
    else:
        print('Failed to read Stick_Image_frame2')
    bottom_camera1.release()
    bottom_camera2.release()

    buffer = [12] #SIDE LED
    ser.write(buffer)
    print('Open Side LED')
    side_camera = cv2.VideoCapture(0)
    side_camera.set(3, 1920)
    side_camera.set(4, 1080)
    time.sleep(1)
    ret2, frame2 = side_camera.read()
    if(ret2 == True):
        cv2.imwrite((raw_folder_path + '/side/side_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame2)
        print('!!Side_Image saved!!')
    else:
        print('Failed to read Side_Image')
    side_camera.release()

    buffer = [14] #TOP LED
    ser.write(buffer)
    print('Open Top LED')
    top_camera = cv2.VideoCapture(2)
    top_camera.set(3, 1920)
    top_camera.set(4, 1080)
    time.sleep(1)
    ret3, frame3 = top_camera.read()
    if(ret3 == True):
        cv2.imwrite((raw_folder_path + '/bottom/bottom_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame3)
        print('!!Bottom_Image saved!!')
    else:
        print('Failed to read Bottom_Image')
    top_camera.release()
    buffer = [104]
    ser.write(buffer)
    time.sleep(3)


buffer = [12] #SIDE LED
ser.write(buffer)
side_camera = cv2.VideoCapture(0)
time.sleep(1)
count = len(os.listdir(raw_folder_path + '/clip'))
path = raw_folder_path + '/clip/clip' + str('0'*(4-len(str(count)))) + str(count)
count = 1
buffer = [104]
ser.write(buffer)
startTime = time.time()*1000
print(path)
os.mkdir(path)
while((time.time()*1000 - startTime) < 7150):
    start = time.time()
    ret, frame = side_camera.read()
    if(ret == True):
        cv2.imwrite((path + '/img_' + str(('0'*(4-len(str(count)))) + str(count)) + '.jpg'), frame)
        print('!!Frame[' + str(count) + '] saved!!')
    count += 1
    print('Runtime : ' + str(start - time.time()) + ' sec.')
side_camera.release()