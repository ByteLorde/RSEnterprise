
import os

import cv2
import imutils as imutils
import numpy as np

cap = cv2.VideoCapture(0)
templates_dir = "../../assets/templates/"
template_array = list(os.listdir(templates_dir))

templates = []

for file in template_array:
    template = cv2.imread(templates_dir + file, 0)
    template = cv2.Canny(template, 50, 200)
    templates.append(template)

orb = cv2.ORB_create()




kps  = []
dess = []
for template in templates:
    kp2, des2 = orb.detectAndCompute(template, None)
    kps.append(kp2)
    dess.append(des2)


while True:

    # _, frame = cap.read()
    frame = cv2.imread("../../assets/templates/inventory.png", 0)
    gray = cv2.Canny(frame, 50, 200)


    for temporary in templates:

        (tH, tW) = temporary.shape[:2]

        found = (0, 0, 0)
        for scale in np.linspace(0.2, 1.0, 20)[::-1]:
            # resize the image according to the scale, and keep track
            # of the ratio of the resizing
            resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
            r = gray.shape[1] / float(resized.shape[1])

            # if the resized image is smaller than the template, then break
            # from the loop
            if resized.shape[0] < tH or resized.shape[1] < tW:
                break

            edged = cv2.Canny(resized, 50, 200)
            result = cv2.matchTemplate(edged, temporary, cv2.TM_CCOEFF)
            (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
            if found is None or maxVal > found[0]:
                found = (maxVal, maxLoc, r)
        (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
        (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
        cv2.imshow("Image", frame)




    cv2.imshow("original", frame)
    cv2.imshow("gray", gray)


    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()