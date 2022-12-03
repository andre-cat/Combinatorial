from tkinter import Widget as tkWidget
from tkinter import Frame as tkFrame
from tkinter import Label as tkLabel
from tkinter import Entry as tkEntry
from tkinter import Text as tkText
from tkinter import Button as tkButton
from tkinter import Canvas as tkCanvas
from tkinter import PhotoImage as tkPhotoImage
from tkinter import font as ttFont
from tkinter.ttk import Widget as ttWidget
from tkinter.ttk import Style as ttStyle
from tkinter.tix import Tk as txTk
from tkinter.tix import TixWidget as txWidget
from typing import Callable


class Frame(tkFrame):
    def __init__(master: tkWidget, bg: str):
        super.__init__(master=master, bg=bg)


class Label(tkLabel):
    def __init__(master: tkWidget, bg: str, fg: str, text: str):
        super.__init__(master=master, bg=bg, fg=fg, font=('Lucida Sans', 14), text=text, anchor='w')


class Title(tkLabel):
    def __init__(master: tkWidget, bg: str, fg: str, text: str):
        super.__init__(master=master, bg=bg, fg=fg, font=('OCR A Extended', 30), text=text, anchor='se')


class Button(tkButton):
    def __init__(master: tkWidget, bg: str, fg: str, text: str, command: Callable):
        super.__init__(master=master, bg=bg, fg=fg, font=('Lucida Sans', 20), text=text, anchor='se', command=command)

