from IrisImageUtils.Shapes.ShapeDetection import *
from src.base.objs.CascadeObject.CascadeObject import CascadeObject
from src.base.objs.DepthPerception import DepthPerception
from src.base.objs.Drawable import Drawable
from src.base.objs.Face.Face import Face
from src.base.objs.Face.FacialRecognition.FacialRecognition import FaceRecognition
from src.base.objs.Frame.Frame import Frame
from src.base.objs.Timer import Timer
from src.base.objs.modules.CannyEdgeDetection.CannyEdgeDetection import CannyEdgeDetection
from src.base.objs.modules.ContourDetection.ContourDetection import ContourDetection
from src.base.objs.modules.Threshold.Threshold import Threshold
from src.base.objs.modules.GaussianBlur.GaussianBlur import GaussianBlur
import os

faceRecognizer = FaceRecognition(FaceRecognition.LBPH)


def main():


    threshold = Threshold()

    template_array = list(os.listdir("../../assets/templates/"))

    blur = GaussianBlur()
    faceDetector = CascadeObject(CascadeObject.FACE_FRONTAL_ALT)
    palmDetector = CascadeObject(CascadeObject.FIST)

    canny = CannyEdgeDetection()
    images = []

    depthPerceptor = DepthPerception.DepthPerception()
    fg = cv2.createBackgroundSubtractorMOG2(history=5)

    contourDetector = ContourDetection()
    eyeDetector = CascadeObject(CascadeObject.EYE)
    timer = Timer(2)
    i = 0

    cap = cv2.VideoCapture(0)
    while True:

        _, frame = cap.read()


        bigImage = Frame(frame)

        mask = fg.apply(frame)
        cv2.imshow("Foreground", mask)
        faceROIs = bigImage.detectFaces()



        faces = []
        for faceROI in faceROIs:
            faces.append(bigImage.grabROI(faceROI))



        for face in faces:

            faceFrame = Face(face.result)
            faceFrame.resize(250, 250)
            faceFrame.result = cv2.cvtColor(faceFrame.result, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Normal", faceFrame.result)
            faceFrame.normalize()
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            faceFrame.result = clahe.apply(faceFrame.result)
            cv2.imshow("Normalized", faceFrame.result)

            labelNo, confidence = faceRecognizer.recognize(faceFrame.result)

            if labelNo == -1:
                break
            name = faceRecognizer.recognizer.getLabelInfo(labelNo)
            bigImage.putText(name + "  " + str(100 - int(confidence)) + "%", face,font=Drawable.Drawable.HERSHEY_SCRIPT_SIMPLEX)
        cv2.imshow("Result", bigImage.result)



        if cv2.waitKey(10) & 0xFF == ord('q'):
            break



    cv2.destroyAllWindows()
    cap.release()

#
#
# def test():
#     IMAGE_PATH = "/home/syndicate/PycharmProjects/Iris/assets/faces/s2/"
#     faces = os.listdir(IMAGE_PATH)
#     face_images = []
#     for face in faces:
#
#         image = cv2.imread(IMAGE_PATH + face, 0)
#
#         face_images.append(image)
#
#     for face in face_images:
#
#         labelNo, confidence = faceRecognizer.recognize(face)
#         print("Label:", labelNo)
#         print("Confidence:", confidence)
#         if labelNo == -1:
#             break
#         name = faceRecognizer.recognizer.getLabelInfo(labelNo)
#         assert name == "Mike"
#
#     print("Images in s2 map to Mike")
#
#     print("\n\n\n")
#     IMAGE_PATH = "/home/syndicate/PycharmProjects/Iris/assets/faces/s1/"
#     faces = os.listdir(IMAGE_PATH)
#     face_images = []
#     for face in faces:
#
#         image = cv2.imread(IMAGE_PATH + face, 0)
#
#         face_images.append(image)
#
#
#     for face in face_images:
#
#         labelNo, confidence = faceRecognizer.recognize(face)
#         if labelNo == -1:
#             break
#         name = faceRecognizer.recognizer.getLabelInfo(labelNo)
#         assert name == "Adam"
#
#     print("Images in s1 map to Adam")

main()