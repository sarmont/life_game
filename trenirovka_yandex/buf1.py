import tkinter as tk

window = tk.Tk(className='Welcome Tkinter!')
window.geometry("500x300")

hello = tk.Label(window, text="Привет, Tkinter!", fg="#fadaaa", bg="black", width=20, height=2, font='Times 30')

name = tk.Entry()
name.insert(0, 'Андрей')

go = tk.Button(text='Press me!')

hello.pack()
name.pack()
go.pack()
window.mainloop()