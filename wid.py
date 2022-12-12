"""
from tkinter import Text
from tkinter import Tk
from tkinter import Label

root = Tk()
root['bg'] = 'white'

text = Text(
    master=root,
    bd=0,
    highlightthickness=0,
    highlightbackground='grey',
    highlightcolor='grey',
    )

readonly = False

if readonly:
    text.configure(
        exportselection=0,
        selectbackground='white',
        selectforeground='black',
        insertbackground='white'
        )
else:
    text.configure(
        exportselection=1,
        selectbackground='lime',
        selectforeground='white',
        insertbackground='lime'
        )

text.insert('end','Hola, ¿cómo estás?')
text.pack(pady=5)

root.mainloop()
"""

from tkinter import Tk
from tkinter import Button as TKButton
from tkinter import LabelFrame as TKLabelFrame

class Button(TKButton):
    def __init__(self, master, text):
        self.label = TKLabelFrame(master=master, bg='black',relief='solid', bd=2, highlightthickness=0)
        TKButton.__init__(
            self,
            master=self.label,
            text=text,
            bd=0,
            bg='white',
            fg='black',
            activebackground='#ededed',
            activeforeground='black'
            )
        super(Button, self).pack()

    def pack(self, *args, **kwargs):
        self.label.pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        self.label.grid(*args, **kwargs)

    def place(self, *args, **kwargs):
        self.label.place(*args, **kwargs)



root = Tk()
root['bg']='white'
root.geometry('250x150')

button = Button(root,text='Holi')
button.grid(column=1, row=1)

root.mainloop()