import cv2
import imutils
from hUMAN_DETECTION import Detector

img = cv2.imread('C:/Users/Fola/Desktop/TOBI/CODES/pedestrian detection/pedestrian 2.jpg')
img = imutils.resize(img, width=700)
img = Detector(img)
cv2.waitKey(0)
cv2.destroyAllWindows()