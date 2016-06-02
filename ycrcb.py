import cv2
import numpy as np

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
	# initialize the dimensions of the image to be resized and
	# grab the image size
	dim = None
	(h, w) = image.shape[:2]

	# if both the width and height are None, then return the
	# original image
	if width is None and height is None:
		return image

	# check to see if the width is None
	if width is None:
		# calculate the ratio of the height and construct the
		# dimensions
		r = height / float(h)
		dim = (int(w * r), height)

	# otherwise, the height is None
	else:
		# calculate the ratio of the width and construct the
		# dimensions
		r = width / float(w)
		dim = (width, int(h * r))

	# resize the image
	resized = cv2.resize(image, dim, interpolation=inter)

	# return the resized image
	return resized

valid = True

lower = np.array([13,50,50], dtype = "uint8")
upper = np.array([16,255,255], dtype = "uint8")

cap = cv2.VideoCapture(0)

fgbg = cv2.BackgroundSubtractorMOG()



while(True) :
    try :
        print "grabbing"
        grabbed, img = cap.read()

    except :
        print "error in capturing"
        valid = False

    if valid == True :
        try :
            #img = resize(img, width=400)
            img = cv2.flip(img,1)

            #converted = cv2.cvtcolor(img, cv2.COLOR_BGR2HSV)
            #skin = cv2.inRange(img,lower,upper)

            skin = fgbg.apply(img)

            #contours, hierarchy = cv2.findContours(skin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            cv2.imshow("images", skin)
            if cv2.waitKey(1) & 0xFF == ord('q') :
                break

        except :
            print "waiting for device"

cap.release()
cv2.destroyAllWindows()
