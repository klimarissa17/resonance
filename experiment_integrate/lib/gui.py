from tkinter import *   ## notice lowercase 't' in tkinter here
class Field:
    def __init__(self, master, text):
        self.frame = Frame(master, background=master['background'])
        self.l = Label(self.frame, text=text, width=10, font=("", 12), background=master['background'])
        self.e = Entry(self.frame, width=10)
        self.l.pack(side=LEFT)
        self.e.pack(side=LEFT)
        self.frame.pack()
    def get(self):
        return self.e.get()

def onButton(event, fields, filename, extra_file, param):
    start = int(fields[0].get())
    end = int(fields[1].get())
    from experiment_integrate.lib.maths import main_calculation
    main_calculation(filename, extra_file, start, end, param)


def button(input_file, extra_file):
    root = Tk()
    root.title("SET PARAMETERS")
    root.configure(background='#afafff')
    root.geometry("300x200")
    color = IntVar()
    red = Radiobutton(text="Red", variable=color, value=0, bg='red', width=20)
    green = Radiobutton(text="Green", variable=color, value=1, bg='green', width=20)
    blue = Radiobutton(text="Blue", variable=color, value=2, bg='blue', width=20)
    red.pack()
    green.pack()
    blue.pack()
    lst = ['from', 'to']
    fields = [Field(root, name) for name in lst]
    b = Button(root, text='DRAW')
    b.bind('<Button-1>', lambda event: onButton(event, fields, input_file, extra_file, color.get() + 1))
    b.pack()

    root.mainloop()


