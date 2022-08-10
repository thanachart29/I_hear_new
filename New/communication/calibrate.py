import cv2

cam = cv2.VideoCapture(4)
# cam1 = cv2.VideoCapture(1)
# cam2 = cv2.VideoCapture(2)
cam.set(3, 1280)
cam.set(4, 720)
# cam1.set(3, 1280)
# cam1.set(4, 720)
# cam2.set(3, 1280)
# cam2.set(4, 720);

while(True):
    ret, frame = cam.read()
    # ret1, frame1 = cam1.read()
    # ret2, frame2 = cam2.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if ret == True:
        for i in range(0, frame.shape[0], int(frame.shape[0]/6)):
            frame = cv2.line(frame,(0, i), (frame.shape[1], i), (0, 0, 0), 2)
            # frame1 = cv2.line(frame1,(0, i), (frame1.shape[1], i), (0, 0, 0), 2)
            # frame2 = cv2.line(frame2,(0, i), (frame2.shape[1], i), (0, 0, 0), 2)
        for i in range(0, frame.shape[1], int(frame.shape[1]/8)):
            frame = cv2.line(frame,(i, 0), (i, frame.shape[0]), (0, 0, 0), 2)
            # frame1 = cv2.line(frame1,(i, 0), (i, frame1.shape[0]), (0, 0, 0), 2)
            # frame2 = cv2.line(frame2,(i, 0), (i, frame2.shape[0]), (0, 0, 0), 2)
        frame = cv2.line(frame,(int(frame.shape[1]/2)-12, int(frame.shape[0]/2)+12), (int(frame.shape[1]/2)+12, int(frame.shape[0]/2)-12), (0, 0, 255), 2)
        frame = cv2.line(frame,(int(frame.shape[1]/2)-12, int(frame.shape[0]/2)-12), (int(frame.shape[1]/2)+12, int(frame.shape[0]/2)+12), (0, 0, 255), 2)
        frame = cv2.flip(frame, 1)
        # frame1 = cv2.line(frame1,(int(frame1.shape[1]/2)-12, int(frame1.shape[0]/2)+12), (int(frame1.shape[1]/2)+12, int(frame1.shape[0]/2)-12), (0, 0, 255), 2)
        # frame1 = cv2.line(frame1,(int(frame1.shape[1]/2)-12, int(frame1.shape[0]/2)-12), (int(frame1.shape[1]/2)+12, int(frame1.shape[0]/2)+12), (0, 0, 255), 2)
        # frame1 = cv2.flip(frame1, 1)
        # frame2 = cv2.line(frame2,(int(frame2.shape[1]/2)-12, int(frame2.shape[0]/2)+12), (int(frame2.shape[1]/2)+12, int(frame2.shape[0]/2)-12), (0, 0, 255), 2)
        # frame2 = cv2.line(frame2,(int(frame2.shape[1]/2)-12, int(frame2.shape[0]/2)-12), (int(frame2.shape[1]/2)+12, int(frame2.shape[0]/2)+12), (0, 0, 255), 2)
        # frame2 = cv2.flip(frame2, 1)
        cv2.imshow('CAM1', frame)
        # cv2.imshow('CAM2', frame1)
        # cv2.imshow('CAM3', frame2)

cam.release()
cv2.destroyAllWindows()

# frame = cv2.imread('/Users/newsogood/Downloads/WIN_20220714_17_27_59_Pro.jpg')

# for i in range(0, frame.shape[0], int(frame.shape[0]/6)):
#     frame = cv2.line(frame,(0, i), (frame.shape[1], i), (0, 0, 0), 2)
# for i in range(0, frame.shape[1], int(frame.shape[1]/8)):
#     frame = cv2.line(frame,(i, 0), (i, frame.shape[0]), (0, 0, 0), 2)
# frame = cv2.line(frame,(int(frame.shape[1]/2)-12, int(frame.shape[0]/2)+12), (int(frame.shape[1]/2)+12, int(frame.shape[0]/2)-12), (0, 0, 255), 2)
# frame = cv2.line(frame,(int(frame.shape[1]/2)-12, int(frame.shape[0]/2)-12), (int(frame.shape[1]/2)+12, int(frame.shape[0]/2)+12), (0, 0, 255), 2)
# frame = cv2.flip(frame, 1)
# while(True):
#     cv2.imshow('CAM1', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()