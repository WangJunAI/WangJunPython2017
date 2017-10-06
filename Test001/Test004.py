import numpy as np  
import cv2  
#import cv2.cv as cv  
from matplotlib import pyplot as plt  
  
face_cascade = cv2.CascadeClassifier('E:\\haarcascade_frontalface_default.xml')  
  
  
img = cv2.imread('E:\\1.jpg')  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
faces = face_cascade.detectMultiScale(
   gray,
   scaleFactor = 1.15,
   minNeighbors = 5,
   minSize = (5,5),
   flags =1
)
print( format(len(faces)))

for(x,y,w,h) in faces:
   cv2.rectangle(img,(x,y),(x+w,y+w),(0,255,0),2)

cv2.imshow('img',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()