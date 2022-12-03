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
from typing import List
from typing import Union
from typing import Callable
from combinatorial.visual.theme import Theme
from combinatorial import constants


class Widgeter:

    pixel: tkPhotoImage

    def __init__(self, window: txTk, themes: list[Theme] = [Theme()]) -> None:
        self.__window = window
        self.__widgets: List[Union[tkWidget, ttWidget, txWidget]] = []
        self.__themes: list[Theme] = themes
        self.__theme: Theme = self.__themes[0]
        self.__number_theme: int = 0
        self.__theme_button: tkButton
        self.__theme_icon: tkPhotoImage

        self.__window.option_add('*TCombobox*Listbox*Font', ttFont.Font(family='Dubai', size=12))
        self.__style = ttStyle(window)

        for theme in self.__themes:
            self.__style.theme_create(theme.back, parent='alt',
                                      settings={
                                          '*': {'configure': {'background': theme.back, 'foreground': theme.fore}},
                                          'TNotebook': {'configure': {'tabmargins': [2, 5, 2, 0], 'background': theme.back, 'borderwidth': 0}},
                                          'TNotebook.Tab': {
                                              'configure': {'padding': [7, 2], 'background': theme.aux1, 'foreground': theme.fore, 'font': ('Century Gothic', 11)},
                                              'map': {'background': [('selected', theme.back)], 'foreground': [('selected', 'black')], 'expand': [('selected', [1, 1, 1, 0])]}},
                                          'TCombobox': {'configure': {'selectbackground': theme.aux1, 'selectforeground': theme.fore, 'fieldbackground': theme.aux1, 'bordercolor': theme.back, 'background': theme.aux2, 'arrowcolor': theme.aux1}}
                                      })

        self.__style.theme_use(self.__theme.back)

        Widgeter.pixel = tkPhotoImage(width=1, height=1)

    def frame(self, master: tkWidget) -> tkFrame:
        frame: tkFrame = tkFrame(master=master, bg=self.__theme.back)
        self.__widgets.append(frame)
        return frame

    def label(self, master: tkWidget, text: str, font_size: int = 14, anchor: str = 'w') -> tkLabel:
        label: tkLabel = tkLabel(master=master, bg=self.__theme.back, fg=self.__theme.fore, font=(self.__theme.sans, font_size), anchor=anchor, text=text)
        self.__widgets.append(label)
        return label

    def title(self, master: tkWidget, text: str) -> tkLabel:
        label: tkLabel = self.label(master=master, anchor='center', text=text)
        label.configure(font=(self.__theme.sans, 30))
        return label

    def button(self, master: tkWidget, command: Callable, text: str = '', font_size: int = 16, photo_path: str = '') -> tkButton:
        button: tkButton = tkButton(master=master, bg=self.__theme.back, fg=self.__theme.fore, command=command, text=text, font=(self.__theme.sans, font_size))
        if photo_path != '':
            photo: tkPhotoImage = tkPhotoImage(file=photo_path)
            button.configure(image=photo)
        self.__widgets.append(button)
        return button

    def menu_button(self, master: tkWidget, ini: tkFrame, end: tkFrame, text: str) -> tkButton:
        button: tkButton = tkButton(master=master, bg=self.__theme.aux1, fg=self.__theme.fore, command=lambda: Widgeter.__go_to_from(end, ini), text=text, relief='flat')
        button.configure(font=(self.__theme.sans, 20))
        return button

    def back_button(self, master: tkWidget, ini: tkFrame, end: tkFrame) -> tkButton:
        button: tkButton = tkButton(master=master, bg=self.__theme.back, fg=self.__theme.fore, command=lambda: Widgeter.__go_to_from(end, ini), text='\u2190', width=50, height=50, font=('Cascadia Code', 30), image=Widgeter.pixel, compound="c", border=0)
        self.__widgets.append(button)
        return button

    def entry(self, master: tkWidget, width: int = 5) -> tkEntry:
        entry: tkEntry = tkEntry(master=master, border=0, width=width, font=(self.__theme.mono, 14, 'bold'), justify='center', fg=self.__theme.fore, bg=self.__theme.aux1, selectforeground=self.__theme.back, selectbackground=self.__theme.aux2, insertbackground=self.__theme.anot)
        self.__widgets.append(entry)
        return entry

    def text(self, master: tkWidget) -> tkText:
        text = tkText(master=master, wrap='word', highlightthickness=0, border=0)
        self.__widgets.append(text)
        return text

    def put_icon_theme(self, master: Union[tkWidget, ttWidget, txWidget]):
        self.__theme_button = tkButton(master=master, bg=self.__theme.back, fg=self.__theme.fore, command=lambda: self.__change_theme(), width=30, height=30, font=('Consolas', 30), image=Widgeter.pixel, compound="c", border=0)
        self.__theme_button.pack(side='top', expand=False, anchor='e', padx=20, pady=20)
        self.__toggle_icon()

        #self.__theme_button = tkButton(master=master, command=lambda: self.__change_theme(), border=0, bg=self.__theme.back, activebackground=self.__theme.fore)
        #self.__theme_button.pack(side='top', expand=False, anchor='e', padx=20, pady=20)
        # self.__toggle_icon()

    def __toggle_icon(self) -> None:
        self.__theme_button.configure(text=self.__theme.icon)
        #self.__theme_icon = tkPhotoImage(file=constants.PATH + f'/resources/images/{self.__theme.icon}').zoom(1).subsample(8)
        #self.__theme_button.configure(bg=self.__theme.back, activebackground=self.__theme.fore, image=self.__theme_icon)

    def __change_theme(self) -> None:

        if len(self.__themes) > 1:

            self.__number_theme = self.__number_theme + 1

            if self.__number_theme > len(self.__themes) - 1:
                self.__number_theme = 0

            self.__theme = self.__themes[self.__number_theme]

            self.__style.theme_use(self.__theme.back)

            for widget in self.__widgets:
                if widget.__class__ == tkEntry:
                    try:
                        widget.configure(
                            fg=self.__theme.fore,
                            bg=self.__theme.aux1,
                            selectforeground=self.__theme.back,
                            selectbackground=self.__theme.aux2,
                            insertbackground=self.__theme.anot
                        )  # type: ignore
                    except (Exception):
                        pass
                else:
                    try:
                        widget.configure(bg=self.__theme.back)  # type: ignore
                    except (Exception):
                        pass

                    try:
                        idget.configure(background=self.__theme.back)  # type: ignore
                    except (Exception):
                        pass

                    try:
                        widget.configure(fg=self.__theme.fore)  # type: ignore
                    except (Exception):
                        pass

                    try:
                        widget.configure(foreground=self.__theme.fore)  # type: ignore
                    except (Exception):
                        pass

        self.__toggle_icon()

    @staticmethod
    def __go_to_from(_to: tkFrame, _from: tkFrame):
        _from.pack_forget()
        _to.pack(expand=True, fill='both')

    @property
    def theme(self):
        return self.__theme

    @property
    def widgets(self):
        return self.__widgets
