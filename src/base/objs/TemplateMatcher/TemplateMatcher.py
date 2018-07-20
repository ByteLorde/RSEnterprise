import imutils
import numpy as np
import cv2
import glob
from matplotlib import pyplot as plt

class TemplateMatcher:

    template = cv2.imread("../../assets/templates/leather.png")

    def __init__(self):
        pass

    def matchTemplate2(self):
        img1 = cv2.imread('../../../../assets/templates/leather.png', 0)    # queryImage
        img2 = cv2.imread('../../../../assets/templates/inventory.png', 0)  # trainImage

        cv2.imshow("src2", img2)
        template = img1
        template = cv2.Canny(template, 50, 200)
        (tH, tW) = template.shape[:2]
        cv2.imshow("Template", template)
        label = ""

        for imagePath in glob.glob("../../../../assets/templates/" + "*.png"):
            image = cv2.imread(imagePath)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            found = None

            for scale in np.linspace(0.2, 1.0, 20)[::-1]:

                resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
                r = gray.shape[1] / float(resized.shape[1])

                if resized.shape[0] < tH or resized.shape[1] < tW:
                    break

                edged = cv2.Canny(resized, 50, 200)
                result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
                (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

                if found is None or maxVal > found[0]:
                    found = (maxVal, maxLoc, r)
                    label = imagePath[imagePath.rindex("/")::]

            (_, maxLoc, r) = found
            (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
            (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
            cv2.putText(image, label, (startX, startY), 1, 1, (255, 255, 255))
            cv2.rectangle(img2, (startX, startY), (endX, endY), (0, 0, 255), 2)
            cv2.putText(img2, label, (startX, startY), 1, 1, (255, 255, 255))
            print(label)
            cv2.imshow("Image", image)
            cv2.imshow("Img2", img2)

            cv2.waitKey(0)

    def matchTemplate(self):
        img1 = cv2.imread('../../../../assets/templates/leather.png', 0)  # queryImage
        img2 = cv2.imread('../../../../assets/templates/inventory.png', 0)  # trainImage

        cv2.imshow("src2", img2)
        template = img1
        template = cv2.Canny(template, 50, 200)
        (tH, tW) = template.shape[:2]
        cv2.imshow("Template", template)
        label = ""

        for imagePath in glob.glob("../../../../assets/templates/" + "*.png"):

            image = cv2.imread(imagePath)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            found = None

            for scale in np.linspace(0.2, 1.0, 20)[::-1]:

                resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
                r = gray.shape[1] / float(resized.shape[1])

                if resized.shape[0] < tH or resized.shape[1] < tW:
                    break


                edged = cv2.Canny(resized, 50, 200)
                result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
                (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)



                if found is None or maxVal > found[0]:
                    found = (maxVal, maxLoc, r)
                    label = imagePath[imagePath.rindex("/")::]


            (_, maxLoc, r) = found
            (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
            (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
            cv2.putText(image, label, (startX, startY), 1, 1, (255, 255, 255))
            cv2.rectangle(img2, (startX, startY), (endX, endY), (0, 0, 255), 2)
            cv2.putText(img2, label, (startX, startY), 1, 1, (255, 255, 255))
            print(label)
            cv2.imshow("Image", image)
            cv2.imshow("Img2", img2)

            cv2.waitKey(0)

    def match(self, image):
        MIN_MATCH_COUNT = 10

        img1 = cv2.imread('../../../../assets/templates/leather.png', 0)  # queryImage
        img2 = cv2.imread('../../../../assets/templates/inventory.png', 0)  # trainImage

        print(img1)
        print(img2)
        # Initiate ORB detector
        orb = cv2.ORB_create()
        # find the keypoints with ORB
        kp1 = orb.detect(img1, None)
        kp2 = orb.detect(img2, None)

        # compute the descriptors with ORB
        kp1, des1 = orb.compute(img1, kp1)
        kp2, des2 = orb.compute(img2, kp2)

        # create BFMatcher object
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        # Match descriptors.
        matches = bf.match(des1, des2)
        # Sort them in the order of their distance.
        matches = sorted(matches, key=lambda x: x.distance)
        # Draw first 10 matches.
        img3 = img2.copy()
        img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], flags=2, outImg=img3)
        plt.imshow(img3), plt.show()

        # draw only keypoints location,not size and orientation
        rep1 = cv2.drawKeypoints(img1, kp1, None, color=(0, 255, 0), flags=0)
        rep2 = cv2.drawKeypoints(img2, kp2, None, color=(0, 255, 0), flags=0)

        plt.imshow(rep1), plt.show()
        plt.imshow(rep2), plt.show()

tm = TemplateMatcher()

tm.matchTemplate()