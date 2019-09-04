import os
import cv2


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

    edges = cv2.Canny(frame, 10, 300)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    im2 = cv2.drawContours(im2, contours, -1, (0, 255, 0), 3)
    cv2.imshow("contours", im2)
    # edges.setTo((255, 0, 255), edges != 0);

    cv2.imshow('Normal Video', frame)
    cv2.imshow('canny', edges)





    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()



