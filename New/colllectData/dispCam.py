import cv2

bottom_camera1 = cv2.VideoCapture(1)

while(True):
    
    while(True):
        ret, frame = bottom_camera1.read()
        if ret == True:
            print("recieved frame")
            cv2.imshow('Bottom Camera 1', frame)
            bottom_camera1.release()
            side_camera = cv2.VideoCapture(0)
            break
    while(True):
        ret1, frame1 = side_camera.read()
        if ret1 == True:
            print("recieved frame")
            cv2.imshow('Side Camera', frame1)
            side_camera.release()
            bottom_camera2 = cv2.VideoCapture(3)
            break
    while(True):
        ret2, frame2 = bottom_camera2.read()
        if ret2 == True:
            print("recieved frame")
            cv2.imshow('Bottom Camera 2', frame2)
            bottom_camera2.release()
            side_camera = cv2.VideoCapture(0)
            bottom_camera1 = cv2.VideoCapture(1)
            break
    if cv2.waitKey(1) == ord('q'):
        break

side_camera.release()
bottom_camera1.release()
cv2.destroyAllWindows()