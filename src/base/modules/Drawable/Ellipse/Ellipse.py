import cv2

import numpy as np

class Ellipse:

    count = 0

    def __init__(self, image):
        self.image = image
        cv2.namedWindow('Ellipse')

        cv2.createTrackbar('CenterX', 'Ellipse', 0, 500, self.update)
        cv2.createTrackbar('CenterY', 'Ellipse', 0, 500, self.update)
        cv2.createTrackbar('Major Axis Length', 'Ellipse', 0, 250, self.update)
        cv2.createTrackbar('Minor Axis Length', 'Ellipse', 0, 250, self.update)
        cv2.createTrackbar('Rotation Angle', 'Ellipse', 0, 360, self.update)

        cv2.createTrackbar('Start Angle', 'Ellipse', 0, 360, self.update)
        cv2.createTrackbar('End   Angle', 'Ellipse', 0, 360, self.update)
        cv2.createTrackbar("Line Type", "Ellipse", 0, 50, self.update)
        cv2.createTrackbar('Thickness', 'Ellipse', -5, 20, self.update)
        cv2.createTrackbar('Shift', 'Ellipse', 0, 30, self.update)



    def update(self, x):
        self.image = np.zeros((1000, 1000, 3), np.uint8)

        self.cx = cv2.getTrackbarPos('CenterX', 'Ellipse')
        self.cy = cv2.getTrackbarPos('CenterY', 'Ellipse')
        self.majorlength = cv2.getTrackbarPos('Major Axis Length', 'Ellipse')
        self.minorlength = cv2.getTrackbarPos('Minor Axis Length', 'Ellipse')
        self.rotationangle = cv2.getTrackbarPos('Rotation Angle', 'Ellipse')

        self.startAngle = cv2.getTrackbarPos('Start Angle', 'Ellipse')
        self.endAngle = cv2.getTrackbarPos('End   Angle', 'Ellipse')
        self.lineType = cv2.getTrackbarPos("Line Type", "Ellipse")
        self.thickness = cv2.getTrackbarPos('Thickness', 'Ellipse')
        self.shift = cv2.getTrackbarPos('Shift', 'Ellipse')
        colors = [(255, 0, 0), (225, 0, 0), (200, 25, 25),
                  (175, 50, 25), (150, 75, 25), (45, 90, 105),
                  (100, 145, 145), (90, 0, 45), (50, 100, 150),
                  (0, 0, 255), (255, 0, 255), (0, 255, 25),
                  (75, 80, 0), (100, 100, 25), (205, 65, 15)]

        for i in range(5):
            cv2.ellipse(self.image, (self.cx, self.cy), (self.majorlength + i * 2, self.minorlength + i * 2),
                        self.rotationangle + 30, self.startAngle, self.endAngle, colors[(Ellipse.count + i) % 15], self.thickness, self.lineType - 1, self.shift)

        Ellipse.count += 1
        if Ellipse.count > 14:
            Ellipse.count = 0



img = np.zeros((1000,1000,3), np.uint8)
ellipse = Ellipse(img)
while(1):


    cv2.imshow('image',ellipse.image)
    k = cv2.waitKey(1) & 0xFF


    if k == 27:
        break


cv2.destroyAllWindows()