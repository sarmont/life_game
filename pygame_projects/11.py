import tkinter
import random


def ch_pos(event):
    if event.keysym == 'Up':
        canvas.move(oval, 0, -10)
    if event.keysym == 'Down':
        canvas.move(oval, 0, 10)
    if event.keysym == 'Right':
        canvas.move(oval, 10, 0)
    if event.keysym == 'Left':
        canvas.move(oval, -10, 0)


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='#FFFFFF', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='red')
master.bind("<KeyPress>", ch_pos)
canvas.pack()
master.mainloop()
