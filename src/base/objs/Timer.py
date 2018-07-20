import time


class Timer():

    def __init__(self, duration):
        super().__init__()
        self.duration    = duration
        self.active      = False
        self.starttime   = None
        self.currenttime = None


    def start(self):

        if self.active:
            self.currenttime = self.getTime()
            print("Difference:", self.getDifference())
            print("Desired:", self.duration)
            if self.isComplete():
                print("Completed!\n\n")
                time.sleep(1)
                self.reset()

        else:
            self.starttime = self.getTime()
            self.active = True

    def reset(self):
        self.active = False
        self.starttime = None

    def isComplete(self):
        return self.getDifference() >= self.duration

    def getDifference(self):
        difference = self.currenttime - self.starttime
        return difference

    def getTime(self):
        return int(time.time())
