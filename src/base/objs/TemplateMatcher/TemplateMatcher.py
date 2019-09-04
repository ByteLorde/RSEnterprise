import imutils
import numpy as np
import cv2

from src.base.objs.template.Template import Template
from src.base.modules.Drawable.point.Point import Point

class TemplateMatcher:

    @staticmethod
    def matchTemplate(source, target, threshold=0.8, multiscale=True):

        sourceImage = source.grayscale()
        targetImage = target.grayscale()

        sourceCanny = cv2.Canny(sourceImage, 50, 200)
        targetCanny = cv2.Canny(targetImage, 50, 200)

        (sourceHeight, sourceWidth) = sourceCanny.shape[:2]
        (targetHeight, targetWidth) = targetCanny.shape[:2]

        cv2.imshow("Source", sourceImage)
        cv2.imshow("Target", targetImage)

        positives = []

        if multiscale:
            for scale in np.linspace(0.2, 1.0, 20)[::-1]:

                resizedImage = imutils.resize(targetImage, width=int(targetWidth * scale))
                (resizedHeight, resizedWidth) = resizedImage.shape[:2]

                r = targetWidth / float(resizedWidth)

                if resizedHeight < targetHeight or resizedWidth < targetWidth:
                    break

                resizedTemplate = Template(resizedImage, "")
                matches  = TemplateMatcher.matchTemplate(source, resizedTemplate, multiscale=False)

                # We must scale the endpoint by the r value for points found doing multiscale matching
                for match in matches:
                    startpoint = match[0]
                    endpoint   = match[1]
                    startpoint.x *= r
                    startpoint.y *= r
                    endpoint.x   *= r
                    endpoint.y   *= r
                    positives += ( startpoint, endpoint )

        result = cv2.matchTemplate(sourceCanny, targetCanny, cv2.TM_CCOEFF)

        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        if maxVal < threshold:
            return positives

        (startX, startY) = (int(maxLoc[0]), int(maxLoc[1]))
        (endX,   endY)   = (int((maxLoc[0] + targetWidth)), int((maxLoc[1] + targetHeight)))

        startPoint = Point(startX, startY)
        endPoint   = Point(endX, endY)

        points = ( startPoint, endPoint )
        positives.append(points)

        return positives

    @staticmethod
    def findTemplate(templates, template, threshold=.75, multiscale=False):
        matches = []
        for item in templates:
            result = TemplateMatcher.matchTemplate(item, template, threshold, multiscale)
            if result:
                matches.append( ( item, result ) )
        return matches


def draw(template, positives, name):
    img = template.image
    print("Positives")
    print(positives)

    for detections in positives:
        (point1, point2) = detections
        cv2.rectangle(img, (point1.x, point1.y), (point2.x, point2.y), (0, 0, 255), 2)
        cv2.putText(img, name, (point1.x, point1.y), 1, 1, (255, 255, 255))

    # cv2.rectangle(img, (p1.x, p1.y), (p2.x, p2.y), (0, 0, 255), 2)

    cv2.imshow(template.getTemplateName(), img)

    cv2.waitKey(0)
tm = TemplateMatcher()

img1 = cv2.imread("leather.png")
img2 = cv2.imread("inventory.png")
source = Template.fromImage(img2, "inventory.png")
target = Template.fromImage(img1, "Leather.png")

r1 = tm.matchTemplate(source, target, multiscale=False)
draw (source, r1, target.getTemplateName())
print("\n")
# r2 = tm.findTemplate([t2], t1)
# draw (t1, r2)


