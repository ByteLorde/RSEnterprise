from faker import Faker
from random import randint

"""
Creates a Bot and stores important information.
TODO: Split class into two: Bot and BotFactory

 @author 2018-08-05 Kaitlyn Lee

 @internal
   @history 2018-08-05 Kaitlyn Lee - Original version.
"""
class Bot:

    """
    Constructs an empty Bot
    """
    def __init__(self):
        self.name = ""
        self.username = ""
        self.password = ""
        self.email = ""
        self.birthday = ""
        self.gender = ""
        self.generator = Faker()

    """
    Generates a random password with a length between 7-15. 
    Lowercase and digits are always on, while special characters and upper case may be on/off.
    """
    def generatePassword(self):
        length = randint(7, 15)
        specialChars = randint(0, 1)
        digits = True
        upperCase = randint(0, 1)
        lowerCase = True

        self.password = self.generator.password(length, specialChars, digits, upperCase, lowerCase)

    """
    Generates a random username, name, email, and gender
    """
    def generateProfile(self):
        profile = self.generator.simple_profile()
        self.username = profile["username"]
        self.name = profile["name"]
        self.email = profile["mail"]
        self.gender = profile["sex"]

        self.generatePassword()
        self.generateBirthday()

    """
    Generates a random birthday between the years 1983-2000
    """
    def generateBirthday(self):
        self.birthday = self.generator.date_between("-35y", "-18y")

    """
    Returns the password
    
    @return String The password
    """
    def getPassword(self):
        return self.password

    """
    Returns the password

    @return String The password
    """
    def getName(self):
        return self.name

    """
    Returns the username

    @return String The username
    """
    def getUsername(self):
        return self.username

    """
    Returns the email

    @return String The email
    """
    def getEmail(self):
        return self.email

    """
    Returns the birthday

    @return String The birthday
    """
    def getBirthday(self):
        return self.birthday

    """
    Returns the gender

    @return String The gender
    """
    def getGender(self):
        return self.gender

