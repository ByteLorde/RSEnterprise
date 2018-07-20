import sys
from asyncio import sleep

import cv2
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QWidget
from PIL import Image

from src.base.objs.Face.Face import Face
from src.base.objs.FaceNormalization.FaceNormalization import FaceNormalizer
from src.base.objs.Frame.Frame import Frame


class ImageProcessor(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Processor")
        self.setGeometry(700, 400, 875, 545)
        self.initComponents()

    def initComponents(self):
        pass



def main():
    facesDir = QDir("/home/syndicate/PycharmProjects/Iris/assets/faces/")

    faceFolders = facesDir.entryList()
    normalizer = FaceNormalizer()

    for folder in faceFolders:
        temp = QDir("/home/syndicate/PycharmProjects/Iris/assets/faces/" + folder)
        temp.setNameFilters(["*.png"])

        images = temp.entryList()
        for image in images:
            path = temp.absoluteFilePath(image)
            image = cv2.imread(path, 0)
            cv2.imshow("image", image)
            print(path)
            frame = Face(image)
            normalized = frame.normalize()
            cv2.imwrite(path, normalized)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                exit(1)


main()