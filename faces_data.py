import cv2
import pandas as pd
import face_recognition as fr

vid = cv2.VideoCapture(0)
fd = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_frontalface_default.xml'
)

try:    
    face_db = pd.read_csv('faces_data.tsv', index_col=0, sep='\t')
    data = {
        'name':face_db['name'].values.tolist(),
        'encoding':face_db['encoding'].values.tolist(),
    }
except Exception as e:
    print(e)
    data = {'name':[], 'encoding':[]}

names=data['name']
enc=data['encoding']
frameLimit=20
frameCount = 0
name = input("Enter your name")
while True:
    flag, img = vid.read()
    if flag:                                                    
        faces = fd.detectMultiScale(
            cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (50,50)
        )
        if len(faces) == 1:
        
            x, y, w, h = faces[0]
            img_face = img[y:y+h, x:x+w, :].copy()
             
            img_face = cv2.resize(img_face, (400,400), interpolation=cv2.INTER_CUBIC)
            face_encoding = fr.face_encodings(img_face)
            if len(face_encoding) == 1:
                enc.append(face_encoding[0].tolist())
                names.append(name)
                frameCount+=1
                print(frameCount)
                if frameCount==frameLimit:
                    data = {'name':names, 'encoding':enc}
                    pd.DataFrame(data).to_csv('faces_data.tsv', sep='\t')
                    break
            
        for(x,y,w,h) in faces:
            cv2.ractangle(
            img
            cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,255),5)
            ci=j[y:y+h,x:x+w]
           )        
        cv2.imshow('Preview',img)
        key = cv2.waitKey(1)
        if key == ord('x'):
            break   
cv2.destroyAllWindows()
vid.release()