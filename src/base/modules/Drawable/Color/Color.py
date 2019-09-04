

class Color:

    @staticmethod
    def RED():
        return Color(90, 0, 0)

    @staticmethod
    def GREEN():
        return Color(0, 90, 0)

    @staticmethod
    def BLUE():
        return Color(0, 0, 90)

    def __init__(self, red=0, green=0, blue=0):
        self._red   = ColorValue(red)
        self._blue  = ColorValue(blue)
        self._green = ColorValue(green)

    def getRed(self):
        return self._red.getValue()

    def getGreen(self):
        return self._green.getValue()

    def getBlue(self):
        return self._blue.getValue()

    def setRed(self, red):
        self._red.setValue(red)

    def setGreen(self, green):
        self._green.setValue(green)

    def setBlue(self, blue):
        self._blue.setValue(blue)

    def lighter(self):
        self._red.lighter()
        self._green.lighter()
        self._blue.lighter()

    def darker(self):
        self._red.darker()
        self._green.darker()
        self._blue.darker()

class ColorValue:


    def __init__(self, value=0):
        self.setValue(value)

    def lighter(self):
        self += 15

    def darker(self):
        self -= 15

    def getValue(self):
        return self._value

    def setValue(self, value):

        assert isinstance(value, int), 'Value must be a number!'

        if value < 0:
            value = 0

        if value > 255:
            value = 255

        self._value = value

    def __eq__(self, value):
        self.setValue(value)

    def __add__(self, value):
        newValue = self.getValue() + value
        self.setValue(newValue)

    def __sub__(self, value):
        newValue = self.getValue() - value
        self.setValue(newValue)