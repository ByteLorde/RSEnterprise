from src.base.modules.Drawable.Color.Color import Color


class Drawable:

    def __init__(self, color=None):
        self._color = color or Color()

    def draw(self, canvas):
        pass

    def getColor(self):
        return self._color

    def setColor(self, newColor):
        self._color = newColor

    def darker(self):
        self._color.darker()

    def lighter(self):
        self._color.lighter()
