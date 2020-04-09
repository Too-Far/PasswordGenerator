from tkinter import *
from tkinter import ttk
from functions import generator, PW_popup
# Give option for user to copy new password
# Display Thank you message upon completion

class PWGenGUI:
    def __init__(self, master):
        self.master = master
        master.title('My password Generator')

        self.label_1 = Label(master, text='How Long Do You Want your Password?')
        self.label_1.grid(row=0)
        self.label_2 = Label(master, text='Enter a Number')
        self.label_2.grid(column =0, row = 2)

        style = ttk.Style()
        style.map("C.TButton",
                foreground=[('pressed', 'red'), ('active', 'red')],
                background=[('pressed', '!disabled', 'black'),
                            ('active', 'red')])
        self.txt = Entry(master)
        self.txt.grid(column=1, row = 2)
        self.txt.focus()

        def clicked():
            len = int(self.txt.get())
            PW = generator(len)
            self.txt.delete(0,'end')
            self.txt.focus()
            return PW_popup('Here is your password!', PW)

        def quit():
            self.master.destroy()

        self.btn_1 = ttk.Button(root, text = 'Click for your password !', command = clicked, style='C.TButton')  

        self.btn_1.grid(row=3, column=1)
        self.btn_2 = ttk.Button(root, text = 'Click to end', command = quit, style='C.TButton')
        self.btn_2.grid(row=3, column=0)


root = Tk()
working_GUI = PWGenGUI(root)
root.mainloop()
