import cv2

class Showable:

    def show(self):
        try:
            if self.result.any():
               cv2.imshow("Class: " + str(self.__class__), self.result)
        except AttributeError:
            print("Object has no result...")

