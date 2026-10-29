import numpy as np
import cv2
import sqlite3
from Mail import sendMail
from thread import start_new_thread
from threading import Thread
import time
import urlparse
from camera import VideoCamera

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

id=0
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX,1,.5,0,2,1)

lag = False
test = 0
start = False
timerfinished = True
Mails = 0
StreamStatus = "0"
StreamStarted = False


def Stream():
    while(True):
        global StreamStatus
        readStreamStatus = open("Stream.txt").read()
        StreamStatus = readStreamStatus
        

def sendMails():
    global start
    global test
    global Mails
    print "[*]Thread Mail start.\n"
    readMails = open("Settings.txt").read()
    print readMails
    readlines = readMails.split(',')
    print readlines
    while Mails < len(readlines):
        if "\n" not in readlines[Mails] and "Settings" not in readMails[Mails]:
            #sendMail(readlines[Mails], 'Security Camera', 'Raspberry pi security camera update', 'img2.jpg')
            Mails += 1
            print readlines[Mails]
        elif "\n" in readlines[Mails]:
            readlines[Mails] = readlines[Mails].replace("\n", "")
            #sendMail(readlines[Mails], 'Security Camera', 'Raspberry pi security camera update', 'img2.jpg')
            Mails += 1
            try:
                print readlines[Mails]
            except:
                continue
    timer(15)
    Mails = 0
    test = 0
    start = False

def timer(zeit):
    print "[*]Thread Timer start.\n"
    time.sleep(zeit)
    print "[*]Timer finished."

def capture(camera):
    while (True):
        global StreamStatus
        global StreamStarted
        if(StreamStatus == "0"):
            global test
            global start
            img = camera.get_cvFrame()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray,1.3,5)
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),2)
                #id, conf=rec.predict(gray[y:y+h,x:x+w])
                #profile = getProfile(id)
                #if(profile != None):
                if(test == 0 and start == False):
                    test = test + 1
                    frame = camera.get_cvFrame()
                    cv2.imwrite(filename='img2.jpg', img=frame)
##                    cv2.cv.PutText(cv2.cv.fromarray(img),"Name: " + str(profile[1]),(x,y+h+20),font,255);
##                    cv2.cv.PutText(cv2.cv.fromarray(img),"Age: " + str(profile[2]),(x,y+h+40),font,255);
##                    cv2.cv.PutText(cv2.cv.fromarray(img),"Gender: " + str(profile[3]),(x,y+h+60),font,255);
##                else:
##                    continue
##                #cv2.cv.PutText(cv2.cv.fromarray(img),"Smile: ",(x,y+h+80),font,255);
##                for(ex,ey,ew,eh) in eyes:
##                    cv2.rectangle(img, (ex,ey), (ex+ew,ey+eh), (0,255,0),2)
##                    #for(sx,sy,sw,sh) in smile:
##                        #cv2.rectangle(img, (sx,sy), (sx+sw,sy+sh), (255,0,0), 2)
##                        #cv2.cv.PutText(cv2.cv.fromarray(img),"Smile: True",(x,y+h+80),font,255);
            if(test == 1 and start == False):
                start = True
                test = test + 1
                start_new_thread(sendMails, ())
            
            cv2.imshow('Frame', img);
            if(cv2.waitKey(1) == ord('q')):
                break;
        else:
            StreamStarted = True
            camera.__del__()
            cv2.destroyAllWindows()
            while(StreamStarted == True):
                global StreamStatus
                if(StreamStatus == "0"):
                    break;
                continue
            capture(VideoCamera())
            
    VideoCamera().__del__()
    cv2.destroyAllWindows()
def run():
    start_new_thread(Stream, ())
    capture(VideoCamera())

run() #TODO delete before running



