import os
import cv2

from src.base.overlay.container.Container import Container

cascPath = "../../assets/cascades/haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)
cascades = []

orb = cv2.ORB_create()

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # ret, frame = video_capture.read()

    cv2.imshow("Frameeee", frame)

    # gray = cv2.imread("CurrentPhoto.png", 0)
    gray = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        frame,
        scaleFactor=1.25,
        minNeighbors=5,
        minSize=(15, 15)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        width = x + w
        height = y + h
        # faceContainer = Container(x, y, width, height)


        cv2.putText(frame, "Face", (x + 10, y - 10), 1, 2, (0, 255, 0), 2)

        face = frame[y: y + h, x: x + w]



    cv2.imshow('Normal Video', frame)



    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()



