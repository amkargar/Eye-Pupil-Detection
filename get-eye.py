import cv2
import sys

#Load Cascades
faces=cv2.CascadeClassifier("face.xml")
eyes=cv2.CascadeClassifier("eye.xml")

#Get input & output file path
input, output = [sys.argv[1], sys.argv[2]]

#result is false by default
result = "False"

#Load the image
frame = cv2.imread(input)

#Change image to grayImage and pass it to the "gray" variable
gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#Detect face from grayImage
face=faces.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in face:
    #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),thickness=3)
    gray_face=gray[y:y+h,x:x+w]
    color_face=frame[y:y+h,x:x+w]

    #Detect eyes from face
    eye=eyes.detectMultiScale(gray_face,1.3,5)

    for (a,b,c,d) in eye:
        #rect = cv2.rectangle(color_face,(a,b),(a+c,b+d),(100,100,100),thickness=3)
        crop_img = color_face[b:b+d,a:a+c]
        imHeight, imWidth, _ = crop_img.shape
        hh = imHeight/3
        ww = imWidth/5
        crop_img = crop_img[int(hh):int(2*hh),int(ww):int(4*ww)]
        cv2.imwrite(output,crop_img)
        result = "True"
        break

#Print the result
print(result)