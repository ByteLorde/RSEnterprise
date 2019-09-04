

class Person:

    def __init__(self):
        pass

    def setName(self, new_name):
        self.name = new_name

    def tellMeYourName(self):
        print( self.name )



name = input("Create your name: ")

person = Person()
person.setName(name)
person.tellMeYourName()
