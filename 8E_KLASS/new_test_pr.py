import tkinter as tk
from tkinter import ttk

def click():
    a = int(a_entry.get())
    b = int(b_entry.get())
    c = int(c_entry.get())

    discrim = b ** 2 - 4 * a * c
    d_num.configure(text=discrim)


window = tk.Tk()
window.geometry('300x200')
window.title('Квадратные уравнения - решитель')

a = tk.Label(window, text='A')
b = tk.Label(window, text='B')
c = tk.Label(window, text='C')
d = tk.Label(window, text='Дискриминант')
d_num = tk.Label(window, text='')
count = tk.Label(window, text='Количество корней')
count_num = tk.Label(window, text='')

btn = tk.Button(window, text='Посчитать', command=click)

a_entry = tk.Entry(window)
b_entry = tk.Entry(window)
c_entry = tk.Entry(window)

a.grid(row=0, column=0)
b.grid(row=1, column=0)
c.grid(row=2, column=0)
d.grid(row=3, column=0)
count.grid(row=4, column=0)

a_entry.grid(row=0, column=1)
b_entry.grid(row=1, column=1)
c_entry.grid(row=2, column=1)
d_num.grid(row=3, column=1)
count_num.grid(row=4, column=1)

btn.grid(row=6, column=0)



window.mainloop()
