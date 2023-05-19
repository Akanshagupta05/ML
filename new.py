import cv2
import numpy as np
v=cv2.VideoCapture(0)
fd=cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_frontalface_default.xml'

)
while(1):
    r,i=v.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2RGB)    
    faces=fd.detectMultiScale(j)
    for(x,y,w,h) in faces:
        cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,255),5)
        ci=j[y:y+h,x:x+w]
        eyes=fd.detectMultiScale(ci)
        for(x1,y1,w1,h1) in eyes:
            cv2.rectangle(i,(x+x1,y+y1),(x+w1+x1,y+h1+y1),(0,0,255),5)
    cv2.imshow('orig',i)   
    k=cv2.waitKey(1)
    if(k==27):
        break
cv2.destroyAllWindows()