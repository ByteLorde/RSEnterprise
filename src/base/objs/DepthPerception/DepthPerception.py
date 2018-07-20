import cv2

class DepthPerception:


    def __init__(self):
        cv2.namedWindow("disparity")
        cv2.createTrackbar('Disparities', 'disparity', 16, 100, lambda x: x)
        cv2.createTrackbar('Size', 'disparity', 15, 100, lambda x: x)

    def getDisparityMap(self, images):

        # if len(images) <= 5:
        #     return
        # dispa = cv2.getTrackbarPos('Disparities', 'disparity')
        # size = cv2.getTrackbarPos('Size', 'disparity')
        # while dispa % 16:
        #     dispa += 1
        #
        # while size % 2 == 0:
        #     size += 1
        #
        # if size < 5:
        #     size = 5
        # stereo = cv2.StereoBM_create(dispa, size)
        #
        # disp = stereo.compute(images[0], images[1], cv2.CV_32F)
        # norm_coeff = 255 / disp.max()
        #
        # cv2.imshow("disparity", disp * norm_coeff / 255)
        disp = cv2.imread("/home/syndicate/PycharmProjects/Iris/assets/faces/s1/Disparity_Image.png", 0)
        return disp

    def getDisparityMap2(self):
        disp = cv2.imread("/home/syndicate/PycharmProjects/Iris/assets/faces/s1/Disparity_Image.png", 0)
        return disp