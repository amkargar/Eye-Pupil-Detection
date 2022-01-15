import cv2
import sys

#Get input file path
input = sys.argv[1]

def load_Image(threshold, type):
    
    #Load the image
    frame = cv2.imread(input)
    #frame = cv2.resize(frame, (128, 128))
    grayed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(grayed, (5, 5), 0)
    thresh = cv2.threshold(blurred, threshold, 255, type)[1]
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    draw_contours(frame,contours)

def draw_contours(frame, contours):
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        (imHeight, imWidth, _) = frame.shape
        ww = imWidth/5
        hh = imHeight/100

        if 3 < w*h < 400 :

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            
            print(x+w/2, ww)

            if (0 < x+w/2 < 2*ww) :
                result = "left"

            if (2*ww < x+w/2 < 3*ww) :

                if (0 < y < 45*hh):
                    result = "top"
                   
                if (45*hh < y < 55*hh):
                    result = "center"

                if (55*hh < y < 100*hh):
                    result = "bottom"


            if  (3*ww < x+w/2 < 5*ww) :
                result = "right"

            cv2.line(frame,(int(ww),0),(int(ww),int(imHeight)),(255,0,0))
            cv2.line(frame,(int(2*ww),0),(int(2*ww),int(imHeight)),(255,0,0))
            cv2.line(frame,(int(3*ww),0),(int(3*ww),int(imHeight)),(255,0,0))
            cv2.line(frame,(int(4*ww),0),(int(4*ww),int(imHeight)),(255,0,0))

            cv2.line(frame,(0,int(45*hh)),(int(imWidth),int(45*hh)),(255,0,0))
            cv2.line(frame,(0,int(55*hh)),(int(imWidth),int(55*hh)),(255,0,0))
            
            print(result)

            break
            
    #cv2.imshow("f", frame)
    #cv2.waitKey(0)
      
load_Image(20, cv2.THRESH_BINARY_INV)