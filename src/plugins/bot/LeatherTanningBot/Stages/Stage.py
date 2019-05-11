import cv2
import os

from src.plugins.Bot.objs.template.Template import Template


class Stage:

    ASSET_PATH = "../assets"

    def __init__(self, path=ASSET_PATH):
        self.settings = dict()
        self.load(path)

    # TODO: Assert that this path exists
    def load(self, path):
        self.path = path
        self.templates = []

        # TODO: assert that the image exists.
        for imagePath in os.listdir(self.path):
            template = Template.fromPath(self.path + "/" + imagePath)
            self.templates.append(template)

    # Potentially have the master image (desktop stream) be a static variable in a static class
    # that we would just grab this image from everytime this is called
    def getProgress(self, image):
        # (index, template) = TemplateMatcher.matchTemplate(self.templates, image)
        # total = len(self.templates)
        # progress = index / total

        return 1

    def evaluate(self, image):
        pass

    def getPath(self):
        return self.path

    def __getitem__(self, item):
        assert item in self.settings, "ERROR: Can't find setting for key: " + item
        return self.settings[item]

s = Stage()
print(s["15"])

class Status:

    UNLOADED = 0
    LOADED   = 1