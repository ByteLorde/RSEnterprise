from tkinter import Tk, Canvas
from random import randint

class OverlayCanvas:

    pass


class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ex = 0
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")

        canvas.create_line(10, 20, 80, 95, fill="blue")
        coord = 10, 50, 240, 210

        self.arc = canvas.create_arc(coord, start=90, extent=self.ex, fill="gray", outline='green', stipple='@transparent.xbm',width=2)

    def move_ball(self):
        self.ex += 3
        canvas.after(10, self.move_ball)
        canvas.itemconfig(self.arc, extent=self.ex)

# initialize root Window and canvas
root = Tk()
root.title("Balls")
root.resizable(True,True)
canvas = Canvas(root, width = 875, height = 545)
canvas.pack()

# create two ball objects and animate them
ball1 = Ball(canvas, 10, 10, 30, 30)
ball2 = Ball(canvas, 60, 60, 80, 80)

ball1.move_ball()
ball2.move_ball()

root.mainloop()