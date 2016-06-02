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



while(True) :
    try :
        print "grabbing"
        grabbed, img = cap.read()

    except :
        print "error in capturing"
        valid = False

    if valid == True :
        try :

            img = cv2.flip(img,1)

            #img = resize(img, width=400)
            print "converting"
            converted = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            print "skinmask"
            skinmask = cv2.inRange(converted, lower, upper)

            print "kernel"
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10,10))
            #print "dilate"
            skinmask = cv2.dilate(skinmask, kernel,iterations = 2)
            #print "erode"
            #skinmask = cv2.erode(skinmask, kernel,iterations = 1)
            
            skinmask = cv2.GaussianBlur(skinmask, (3,3), 0)

            

            
            cv2.imshow("images", skinmask)
            if cv2.waitKey(1) & 0xFF == ord('q') :
                break

        except :
            print "waiting for device"

cap.release()
cv2.destroyAllWindows()
