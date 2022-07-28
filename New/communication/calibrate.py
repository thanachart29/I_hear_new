import cv2

cam = cv2.VideoCapture(0)

while(True):
    ret, frame = cam.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if ret == True:
        for i in range(0, frame.shape[0], int(frame.shape[0]/6)):
            frame = cv2.line(frame,(0, i), (frame.shape[1], i), (0, 0, 0), 2)
        for i in range(0, frame.shape[1], int(frame.shape[1]/8)):
            frame = cv2.line(frame,(i, 0), (i, frame.shape[0]), (0, 0, 0), 2)
        frame = cv2.line(frame,(int(frame.shape[1]/2)-12, int(frame.shape[0]/2)+12), (int(frame.shape[1]/2)+12, int(frame.shape[0]/2)-12), (0, 0, 255), 2)
        frame = cv2.line(frame,(int(frame.shape[1]/2)-12, int(frame.shape[0]/2)-12), (int(frame.shape[1]/2)+12, int(frame.shape[0]/2)+12), (0, 0, 255), 2)
        frame = cv2.flip(frame, 1)
        cv2.imshow('CAM1', frame)

cam.release()
cv2.destroyAllWindows()