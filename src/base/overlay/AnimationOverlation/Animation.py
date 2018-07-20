import threadsafe_tkinter as Tkinter


top = Tkinter.Tk()

C = Tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210

    arc = C.create_arc(coord, start=0, extent=ex, fill="red")
    C.after(100, move_ball)

C.pack()
move_ball()
top.mainloop()