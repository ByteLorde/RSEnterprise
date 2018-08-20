import os
import cv2

from RSEnterprise.src.base.objs.TemplateMatcher.TemplateMatcher import TemplateMatcher


class StageReader:

    def __init__(self, path):
        super(StageReader, self).__init__()
        self.templateMatcher = TemplateMatcher()
        self.load(path)
        self.templateMatcher.setPath(self.path)
        self.templateMatcher.load(self.path)


    def load(self, path):
        self.path = path
        self.templates = []

        # TODO: assert that the image exists.
        for imagePath in os.listdir(self.path):
            template = cv2.imread(imagePath)
            self.templates.append(template)


        self.numStages = len(self.templates)


    def evaluate(self, image):
        stage = self.templateMatcher
        self.templateMatcher.matchTemplate(image)


    def getStep(self):
        return self.step

    def setStep(self, step):
        self.step = step

    def getPath(self):
        return self.path

    # TODO: Make this throw an assert error if this path doesn't exist
    def setPath(self, path):
        self.load(path)