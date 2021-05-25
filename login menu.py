from tkinter import *


tkw = Tk()
cvs = Canvas(width="400", height="350", background="#5ca113")


"""
FIRST ROW BUTTONS
"""
cvs.create_arc(70, 45, 250, 265, fill="#a3ccda", outline="#a0ccdb")
cvs.create_text(140, 150, text="Login", font="Helvatica 45 bold", state="normal")
btnScott = Button(tkw, text="Not password and username (Just Tap)", font=" 12", command="scott", bg="#a0ccda")
btnScott.place(x=100, y=275, width="300", height="50")



cvs.pack()
cvs.mainloop()