from src.base.overlay.Component.Component import Component


class Container(Component):

    def __init__(self, label="Container"):
        super(Container, self).__init__(label=label)
        self.children = []

    def addChild(self, child):
        child.setParent(self)
        self.children.append(child)

    def removeChild(self, child):
        if child in self.children:
            child.removeParent(self)
            self.children.remove(child)

    def getChildren(self):
        return self.children

    def drawComponent(self, image):
        for child in self.children:
            child.drawComponent(image)