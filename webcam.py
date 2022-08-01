import cv2
def take_snapshot():
    videocaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptureObject.read()
        cv2.imwrite("newpicture1.jpg",frame)
        result=False

    videocaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()
