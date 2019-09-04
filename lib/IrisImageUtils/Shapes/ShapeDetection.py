import cv2


def get_shape(contour):
    # initialize the shape name and approximate the contour
    shape = "?"
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

    # if the shape is a triangle, it will have 3 vertices
    if len(approx) == 3:
        shape = "Triangle"

    # if the shape has 4 vertices, it is either a square or
    # a rectangle
    elif len(approx) == 4:
        # compute the bounding box of the contour and use the
        # bounding box to compute the aspect ratio
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)

        # a square will have an aspect ratio that is approximately
        # equal to one, otherwise, the shape is a rectangle
        shape = "Square" if ar >= 0.95 and ar <= 1.05 else "Box"

    # if the shape is a pentagon, it will have 5 vertices
    elif len(approx) == 5:
        shape = "Pentagon"


    # return the name of the shape
    return shape