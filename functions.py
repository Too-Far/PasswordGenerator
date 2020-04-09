import random
from tkinter import *
from tkinter import ttk
import pyperclip

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@$%^&*,./?'
def generator(len):
    password = ''
    for _ in range(len):
        password += random.choice(chars)
    return password

def PW_popup(title, message):
    root = Tk()
    root.title(title)
    w = 400     # popup window width
    h = 200     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    w = Label(root, text=m, width=120, height=10)
    w.pack()
    def clicked():
        pyperclip.copy(message)
        root.destroy()
    style = ttk.Style()
    style.map("C.TButton",
            foreground=[('pressed', 'red'), ('active', 'red')],
            background=[('pressed', '!disabled', 'black'),
                        ('active', 'red')])
    b = ttk.Button(root, text='Click Here to Copy', command=clicked, style='C.TButton')
    b.pack()

    # b2 = Button(root, text='Click Here to Copy', command=clicked, width=10)
    # b2.pack()
    #Figure out how to command program to copy password with button click



