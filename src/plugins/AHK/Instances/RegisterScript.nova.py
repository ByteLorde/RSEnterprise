from src.plugins.AHK.NovaScript.NovaScript import NovaScript


class RegisterScript(NovaScript):

    def __init__(self):

        parameters = [
                    "window_x",
                     "window_y",
                     "window_width",
                     "window_height",
                     "title"
                     ]

        self.parameters = dict()

        for parameter in parameters:
            self.parameters[parameter] = None

        self.parameters["title"] = "Register Script"


    def write(self):
        print(self.parameters)


rd = RegisterScript
