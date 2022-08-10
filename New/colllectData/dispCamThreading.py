import threading
import cv2

def side_camera_disp():
    side_camera = cv2.VideoCapture(0)
    while not(side_camera.isOpened()):
        pass
    print('side_camera is opened.')
    while(True):
        ret1, frame1 = side_camera.read()
        if ret1 == True:
            print("recieved frame")
            cv2.imshow('Side Camera', frame1)
        if cv2.waitKey(1) == ord('q'):
            side_camera.release()
            break

def bottom_camera1_disp():
    bottom_camera1 = cv2.VideoCapture(1)
    while not(bottom_camera1.isOpened()):
        pass
    print('bottom_camera1 is opened.')
    while(True):
        ret2, frame2 = bottom_camera1.read()
        if ret2 == True:
            print("recieved frame")
            cv2.imshow('Bottom Camera 1', frame2)
        if cv2.waitKey(1) == ord('q'):
            bottom_camera1.release()
            break

def bottom_camera2_disp():
    bottom_camera2 = cv2.VideoCapture(3)
    while not(bottom_camera2.isOpened()):
        pass
    print('bottom_camera2 is opened.')
    while(True):
        ret3, frame3 = bottom_camera2.read()
        if ret3 == True:
            print("recieved frame")
            cv2.imshow('Bottom Camera 2', frame3)
        if cv2.waitKey(1) == ord('q'):
            bottom_camera2.release()
            break

side_cam_thread = threading.Thread(target=side_camera_disp)
bottom_cam1_thread = threading.Thread(target=bottom_camera1_disp)
bottom_cam2_thread = threading.Thread(target=bottom_camera2_disp)

side_cam_thread.start()
bottom_cam1_thread.start()
bottom_cam2_thread.start()

side_cam_thread.join()
bottom_cam1_thread.join()
bottom_cam2_thread.join()

cv2.destroyAllWindows()