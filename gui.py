from tkinter import *   ## notice lowercase 't' in tkinter here
from easy import integrate
from easy import draw
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


root = Tk()

root.title("TEST")
root.configure(background='#afafff')
# root.geometry("800x600")
lst =  ['m', 'b0', 'w', 'y0', 'axx', 'ayy', 'azz', 'discr']
fields = {name: Field(root, name) for name in lst}

l = Label(root, fg='red', bg='black', text='2000', font=("", 20))
b = Button(root, text="DRAW")

def onButton(event, fields):
    l['text'] = 'Starting...'
    l.update()
    params = {i[0]: float(i[1].get()) for i in fields.items() if i[1].get() != ''}
    num = 100
    foo = lambda  x: x/10
    draw(num, foo, integrate(num, foo, **params))



b.bind('<Button-1>', lambda event:onButton(event, fields))


b.pack()
l.pack()
root.mainloop()