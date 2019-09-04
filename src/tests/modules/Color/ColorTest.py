from src.base.modules.Drawable.Color.Color import Color


def runTestingSuite():
    colorDarkerShouldCapAt0()
    colorLighterShouldCapAt255()
    colorShouldSetColorsToMinOf0()
    colorDarkerShouldIncreaseColor()
    colorShouldSetColorsToMaxOf255()
    colorLighterShouldIncreaseColor()
    colorShouldLoadColorsBasedOnConstructor()
    colorShouldSetColorsWithoutOverridingColorValueObject()

def colorShouldLoadColorsBasedOnConstructor():

    color = Color()

    assert color.getRed()   == 0, 'Actual: ' + str(color.getRed())
    assert color.getBlue()  == 0, 'Actual: ' + str(color.getBlue())
    assert color.getGreen() == 0, 'Actual: ' + str(color.getGreen())

    color = Color(50, 100, 200)

    assert color.getRed()   == 50,  'Actual: ' + str(color.getRed())
    assert color.getBlue()  == 200, 'Actual: ' + str(color.getBlue())
    assert color.getGreen() == 100, 'Actual: ' + str(color.getGreen())


def colorShouldSetColorsWithoutOverridingColorValueObject():
    color = Color()

    color.setRed(200)
    assert color.getRed() == 200, 'Actual: ' + str(color.getRed())

    color.setGreen(100)
    assert color.getGreen() == 100, 'Actual: ' + str(color.getGreen())

    color.setBlue(50)
    assert color.getBlue() == 50, 'Actual: ' + str(color.getBlue())


def colorShouldSetColorsToMaxOf255():
    color = Color()

    color.setRed(256)
    assert color.getRed() == 255, 'Actual: ' + str(color.getRed())

    color.setGreen(300)
    assert color.getGreen() == 255, 'Actual: ' + str(color.getGreen())

    color.setBlue(10000)
    assert color.getBlue() == 255, 'Actual: ' + str(color.getBlue())

def colorShouldSetColorsToMinOf0():
    color = Color()

    color.setRed(-1)
    assert color.getRed() == 0, 'Actual: ' + str(color.getRed())

    color.setGreen(-200)
    assert color.getGreen() == 0, 'Actual: ' + str(color.getGreen())

    color.setBlue(-10000)
    assert color.getBlue() == 0, 'Actual: ' + str(color.getBlue())


def colorLighterShouldIncreaseColor():
    color = Color()

    color.setRed(10)
    color.setBlue(20)
    color.setGreen(30)

    color.lighter()

    assert color.getRed() > 10,   'Actual: ' + str(color.getRed())
    assert color.getBlue() > 20,  'Actual: ' + str(color.getBlue())
    assert color.getGreen() > 30, 'Actual: ' + str(color.getGreen())

def colorDarkerShouldIncreaseColor():
    color = Color()

    color.setRed(10)
    color.setBlue(20)
    color.setGreen(30)

    color.darker()

    assert color.getRed() < 10,   'Actual: ' + str(color.getRed())
    assert color.getBlue() < 20,  'Actual: ' + str(color.getBlue())
    assert color.getGreen() < 30, 'Actual: ' + str(color.getGreen())


def colorLighterShouldCapAt255():
    color = Color()

    color.setRed(255)
    color.setBlue(255)
    color.setGreen(255)

    for i in range(10):
        color.lighter()

    assert color.getRed()   == 255, 'Actual: ' + str(color.getRed())
    assert color.getBlue()  == 255, 'Actual: ' + str(color.getBlue())
    assert color.getGreen() == 255, 'Actual: ' + str(color.getGreen())

def colorDarkerShouldCapAt0():
    color = Color()

    color.setRed(0)
    color.setBlue(0)
    color.setGreen(0)

    for i in range(10):
        color.darker()

    assert color.getRed()   == 0, 'Actual: ' + str(color.getRed())
    assert color.getBlue()  == 0, 'Actual: ' + str(color.getBlue())
    assert color.getGreen() == 0, 'Actual: ' + str(color.getGreen())

if __name__ == '__main__':
    runTestingSuite()
