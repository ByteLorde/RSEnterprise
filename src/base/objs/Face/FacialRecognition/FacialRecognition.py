import cv2
import os
import numpy as np



class FaceRecognition:

    EIGEN  = 0
    FISHER = 1
    LBPH   = 2

    IMAGE_PATH = "/home/syndicate/PycharmProjects/Iris/assets/faces/"


    def __init__(self, type):
        creation_dictionary = \
        {
            FaceRecognition.EIGEN : cv2.face.createEigenFaceRecognizer(threshold=10, num_components=10),
            FaceRecognition.FISHER: cv2.face.createFisherFaceRecognizer(threshold=10, num_components=10),
            FaceRecognition.LBPH  : cv2.face.createLBPHFaceRecognizer(threshold=100)
        }
        self.recognizer = creation_dictionary[type]
        self.createLabels()

    def createLabels(self):

        dirs = os.listdir(FaceRecognition.IMAGE_PATH)
        faces   = []
        IDs     = []

        names=["Adam", "Mike"]
        self.recognizer.setLabelInfo(1, "Adam")
        self.recognizer.setLabelInfo(2, "Chelsea")
        self.recognizer.setLabelInfo(3, "Mike")

        for dir_name in dirs:

            subject_dir_path = FaceRecognition.IMAGE_PATH + "/" + dir_name

            subject_images_names = os.listdir(subject_dir_path)

            for image_name in subject_images_names:

                image_path = subject_dir_path + "/" + image_name

                image = cv2.imread(image_path, 0)
                print(image_path)
                label = int(image_name[0:image_name.rindex(";")])

                faces.append(image)
                IDs.append(label)


        # for person in personFolders:
        #     label = int(person.replace("s", ""))
        #
        #     path = FaceRecognition.IMAGE_PATH + person
        #
        #     faceImages = os.listdir(path)
        #     for faceImage in faceImages:
        #         face = cv2.imread(path + "/" + faceImage, 0)
        #         faces.append(face)
        #         IDs.append(label)
        #         try:
        #             name = faceImage[0: faceImage.index(" ")]
        #         except:
        #             name = faceImage[0: faceImage.index("-")]
        #         print("Name:",name)
        #         self.recognizer.setLabelInfo(label, name)
        #         self.recognizer.getLabelInfo(label)

        self.recognizer.train(np.asarray(faces), np.asarray(IDs) )

    def recognize(self, image):
        return self.recognizer.predict(image)





