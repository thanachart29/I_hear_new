import cv2

def countCameras():
    n = 0
    for i in range(10):
        try:
            cap = cv2.VideoCapture(i)
            ret, frame = cap.read()
            cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cap.release()
            cv2.destroyAllWindows()
            n += 1
        except:
            cap.release()
            cv2.destroyAllWindows()
            break
    return n

cam = []
count = countCameras()
print ('Count of Cam : ' + str(count))

for i in range(count):
    cam.append(cv2.VideoCapture(i))
    cam[i].set(3, 1280)
    cam[i].set(4, 720)

while True:
    for i in range(count):
        ret1, frame1 = cam[i].read()
        if (ret1):
            cv2.imshow('Cam' + str(i+1), frame1)
    if cv2.waitKey(1) == ord('q'):
        break

for i in range(count):
    cam[i].release()
cv2.destroyAllWindows()