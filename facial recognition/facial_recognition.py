import cv2
import sys

# LOAD FACIAL CLASSIFIER
#haarcascade is a sort of classifier these are handcrafted features extracted in
# similar way to deep learning in that you have a bunch of image that would contain
# a face and it is able to recognise the faces we have in webcam
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Open default camera
video_capture = cv2.VideoCapture(0)

#loop video to find faces and make rectangular frame
while True:

    #Capture frame by frame
    retval, frame = video_capture.read()

    #Takes time to process if we use RGB color panel that's why we use grey scale

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize = (35,35)
    )

    #now draw rectangle around the faces

    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y) ,(x+w,x+h), (50,50,200), 2)

#Show frame on video with the frame
    cv2.imshow('Video', frame)

#For exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        sys.exit()
