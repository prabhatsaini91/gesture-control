import cv2

def diffImg(t0, t1, t2) :
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)

valid = True

cam = cv2.VideoCapture(0)

if not cam.isOpened() :
    print "can't open camera"


while valid :
    try :
        winName = "Movement Indicator"
        cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)
        # Read three images first:
        t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
        t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
        t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
        valid = False
        
    except :
        print "waiting for camera"


while True :
    cv2.imshow( winName, diffImg(t_minus, t, t_plus) )
    # Read next image
    t_minus = t
    t = t_plus
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

cam.release()
cv2.destroyAllWindows()
print "Goodbye"


            
