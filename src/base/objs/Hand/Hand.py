import cv2

from src.base.objs.modules.ContourDetection.ContourDetection import ContourDetection

class Hand:


    cd = ContourDetection()
    fg = cv2.createBackgroundSubtractorMOG2(history=10,varThreshold=16,detectShadows=True)
    def DetectHand(_, frame):

        mask = frame.getMask()
        gray = frame.grayscale()
        blur = cv2.medianBlur(gray, 5)
        blur = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY, 11, 2)
        foregroundMask = Hand.fg.apply(blur)
        cv2.imshow("fg", foregroundMask)
        cv2.imshow("Blur", blur)
        _, contours, hierarchy = cv2.findContours(blur, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]


        squares = []
        for c in contours:
            # approximate the contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)

            # if our approximated contour has four points, then we
            # can assume that we have found our screen
            if len(approx) == 4:
                squares.append(approx)
                break


        for square in squares:
            temp = cv2.getPerspectiveTransform(square, temp)
        cv2.drawContours(mask, squares, -1, (255, 50, 50), 2)

        print(len(contours))

        mask1 = mask.copy()
        mask2 = mask.copy()
        mask3 = mask.copy()
        cv2.drawContours(mask, contours, -1, (0, 255, 0), 2)
        cv2.drawContours(mask1, contours, 0, (0, 255, 0), 2)

        cv2.imshow("mask", mask)
        cv2.imshow("mask1", mask1)



