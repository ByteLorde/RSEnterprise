



class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def origin(self):
        return (self.x, self.y)

    def translateX(self, translation):
        self.x += translation

    def translateY(self, translation):
        self.y += translation
