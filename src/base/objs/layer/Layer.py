from src.base.modules.Drawable.Color.Color import Color
from src.base.modules.drawable.Drawable import Drawable


class Layer(Drawable):

    def __init__(self, name='', color=None, zIndex=0, hidden=False, colorOverride=False):

        defaultColor = color or Color.GREEN()
        super().__init__(defaultColor)

        self.setLayerName(name)
        self.setZIndex(zIndex)
        self._hidden = hidden
        self.setOverrideDefaultColors(colorOverride)
        self.clear()

    def draw(self, canvas):
        if not canvas or self.isHidden():
            return

        super(canvas)

        for drawable in self._content:
            drawable.draw(canvas)


    def clear(self):
        self.setContent([])

    def getContent(self):
        return self._content

    def setContent(self, content):
        self._content = content

    def setOverrideDefaultColors(self, override):

        if not isinstance(override, bool):
            return

        self._colorOverride = override

    def getLayerName(self):
        return self._name

    def setLayerName(self, name):
        self._name = name

    def getZIndex(self):
        return self._zIndex

    def setZIndex(self, zIndex):

        if not zIndex:
            return

        if not isinstance(zIndex, int):
            return

        self._zIndex = zIndex

    def hideLayer(self):
        self._hidden = True

    def showLayer(self):
        self._hidden = False

    def isHidden(self):
        return self._hidden
