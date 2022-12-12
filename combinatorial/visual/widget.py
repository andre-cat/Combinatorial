from tkinter import Tk as TKTk
from tkinter import Frame as TKFrame
from tkinter import Label as TKLabel
from tkinter import Entry as TKEntry
from tkinter import Button as TKButton
from tkinter import LabelFrame as TKLabelFrame
from tkinter import PhotoImage as TKPhotoImage
from tkinter import Text as TKText
from tkinter import Toplevel as TKToplevel
from tkinter import Spinbox as TKSpinBox
from tkinter import OptionMenu as TKOptionMenu
from tkinter import StringVar as TKStringVar
from tkinter import Canvas as TKCanvas
from tkinter.messagebox import Message as TKMessage
from abc import ABC
from abc import abstractmethod
from combinatorial.visual.theme import Theme


class Widget(ABC):

    def __init__(self) -> None:
        Widgeter().widgets.append(self)

    def exists(self, attribute: str) -> bool:
        try:
            self.cget(attribute.lower())
            return True
        except Exception as e:
            return False

    @abstractmethod
    def colorize(self) -> None:
        ...

class Widgeter:
    def __new__(self) -> None:
        if not hasattr(self, 'instance'):
            self.instance: 'Widgeter' = super(Widgeter, self).__new__(self)
            self.__widgets: list[Widget] = []
            self.__themes: list[Theme] = [Theme()]
            self.__number_theme: int = 0
            self.__theme: Theme = self.__themes[self.__number_theme]
        return self.instance

    @property
    def widgets(self) -> list[Widget]:
        return self.__widgets

    @property
    def themes(self) -> list[Theme]:
        return self.__themes

    @themes.setter
    def themes(self, themes: list[Theme]) -> None:
        self.__themes = themes

    @property
    def theme(self) -> Theme:
        return self.__theme

    def next_theme(self) -> None:
        self.__number_theme = self.__number_theme + 1
        if self.__number_theme == len(self.__themes):
            self.__number_theme = 0
        self.__theme = self.__themes[self.__number_theme]


def init_widget(function : callable) -> callable:
    def inner_function(self : Widget, *args, **kwargs):
        Widget.__init__(self)
        function(self, *args, **kwargs)
    return inner_function

class Root(Widget, TKTk):
    @init_widget
    def __init__(self, title: str, w: int, h: int) -> None:
        TKTk.__init__(self)
        x: int = (int)(self.winfo_screenwidth() / 2 - w / 2)
        y: int = (int)(self.winfo_screenheight() / 2 - h / 2)
        self.geometry(f'{w}x{h}+{x}+{y}')
        self.resizable(True, True)
        self.title(title)
        self.colorize()

    def colorize(self) -> None:
        self['bg'] = Widgeter().theme.back


class Frame(Widget, TKFrame):
    @init_widget
    def __init__(self, master: Widget, bg=Widgeter().theme.back, w: int = 0, h: int = 0) -> None:
        TKFrame.__init__(
            self,
            master=master,
            width=w,
            height=h
        )
        self.colorize()
        self.config(bg=bg)

    def colorize(self) -> None:
        self['bg'] = Widgeter().theme.back

class Label(Widget, TKLabel):

    @init_widget
    def __init__(self, master: Widget, text: str, w: int = 5) -> None:
        TKLabel.__init__(
            self,
            master=master,
            text=text,
            font=(Widgeter().theme.sans, Widgeter().theme.s),
            justify='left',
            width=w
        )
        self.colorize()

    def colorize(self) -> None:
        self['bg'] = Widgeter().theme.back
        self['fg'] = Widgeter().theme.fore


class Title(Widget, TKLabel):

    @init_widget
    def __init__(self, master: Widget, text: str) -> None:
        TKLabel.__init__(
            self,
            master=master,
            text=text,
            font=(Widgeter().theme.seri, Widgeter().theme.l),
            justify='center'
        )
        self.colorize()

    def colorize(self) -> None:
        self['bg'] = Widgeter().theme.back,
        self['fg'] = Widgeter().theme.fore


class Entry(Widget, TKEntry):
    @init_widget
    def __init__(self, master: Widget, width: int = 5) -> None:
        TKEntry.__init__(
            self,
            master=master,
            width=width,
            font=(Widgeter().theme.mono, Widgeter().theme.s, 'bold'),
            justify='center',
            highlightthickness=2,
            bd=0
        )
        self.colorize()

    def colorize(self) -> None:
        self['bg'] = Widgeter().theme.aux1,
        self['fg'] = Widgeter().theme.fore,
        self['highlightbackground'] = Widgeter().theme.aux1,
        self['highlightcolor'] = Widgeter().theme.aux2,
        self['selectbackground'] = Widgeter().theme.aux2,
        self['selectforeground'] = Widgeter().theme.back,
        self['insertbackground'] = Widgeter().theme.aux2,


class Button(Widget, TKButton):
    @init_widget
    def __init__(self, master: Widget, text: str, command: callable) -> None:
        self.__box = TKFrame(master=master,highlightthickness=2,bd=0)
        TKButton.__init__(
            self,
            master=self.__box,
            command=command,
            text=text,
            font=(Widgeter().theme.mono, Widgeter().theme.s),
            bd=0,
        )
        super(Button, self).pack()
        self.colorize()

    def colorize(self) -> None:
        self.__box['highlightbackground']=Widgeter().theme.fore
        self['bg'] = Widgeter().theme.back,
        self['fg'] = Widgeter().theme.fore,
        self['activebackground'] = Widgeter().theme.aux1,
        self['activeforeground'] = Widgeter().theme.fore

    @property
    def bd(self, bg) :
        return self.__box['bg']

    @bd.setter
    def bd(self, bg) :
        self.__box['bg']=bg

    def pack(self, *args, **kwargs) -> None:
        self.__box.pack(*args, **kwargs)

    def grid(self, *args, **kwargs) -> None:
        self.__box.grid(*args, **kwargs)

    def place(self, *args, **kwargs) -> None:
        self.__box.place(*args, **kwargs)


class MenuButton(Widget, TKButton):
    @init_widget
    def __init__(self, master: Widget, text: str, from_: Frame, to: Frame) -> None:
        TKButton.__init__(
            self,
            master=master,
            command=lambda: ...,
            text=text,
            font=(Widgeter().theme.sans, Widgeter().theme.m),
            bd=0
        )
        make_frame_changer(button=self, from_=from_, to=to)
        self.colorize()

    def colorize(self) -> None:
        self['bg'] = Widgeter().theme.aux1
        self['fg'] = Widgeter().theme.fore
        self['activebackground'] = Widgeter().theme.back
        self['activeforeground'] = Widgeter().theme.fore


class BackButton(Widget, TKButton):
    @init_widget
    def __init__(self, master: Widget, from_: Frame, to: Frame) -> None:
        TKButton.__init__(
            self,
            master=master,
            command=lambda: ...,
            text='←',
            font=('Consolas', 30),
            bd=0
        )
        make_frame_changer(button=self, from_=from_, to=to)
        make_pixel_size(button=self, w=40, h=40)
        self.colorize()

    def colorize(self) -> None:
        self['bg'] = Widgeter().theme.back
        self['fg'] = Widgeter().theme.fore
        self['activebackground'] = Widgeter().theme.aux1
        self['activeforeground'] = Widgeter().theme.fore

class Text(Widget, TKText):
    @init_widget
    def __init__(self, master: Widget, font_sizes: list[int], border: bool = True, readonly: bool = True) -> None:
        self.__readonly = readonly
        TKText.__init__(
            self,
            master=master,
            highlightthickness=2 if border == True else 0,
            bd=0
        )
        self.colorize()
        for size in font_sizes:
            self.tag_configure(f'{size}n', font=('Consolas', size))
            self.tag_configure(f'{size}b', font=('Consolas', size, 'bold'))
            self.tag_configure(f'{size}i', font=('Consolas', size, 'italic'))
            self.tag_configure(f'{size}bi', font=('Consolas', size, 'bold', 'italic'))

    def colorize(self) -> None:
        self['bg'] = Widgeter().theme.back
        self['fg'] = Widgeter().theme.fore
        self['highlightbackground'] = Widgeter().theme.fore
        self['highlightcolor'] = Widgeter().theme.fore

        if self.__readonly:
            self['exportselection'] = 0,
            self['selectbackground'] = Widgeter().theme.back
            self['selectforeground'] = Widgeter().theme.fore
            self['insertbackground'] = Widgeter().theme.back
        else:
            self['exportselection'] = 1
            self['selectbackground'] = Widgeter().theme.aux2
            self['selectforeground'] = Widgeter().theme.back
            self['insertbackground'] = Widgeter().theme.aux2

    def __make_writeable(write_function) -> callable:
        def function(self: 'Text', font_size: int, text: str) -> None:
            self.configure(state='normal')
            write_function(self, font_size, text)
            self.configure(state='disabled')
        return function

    @__make_writeable
    def write(self, font_size: int, text: str) -> None:
        self.insert('end', text, f'{font_size}n')

    @__make_writeable
    def write_bold(self, font_size: int, text: str) -> None:
        self.insert('end', text, f'{font_size}b')

    @__make_writeable
    def write_italic(self, font_size: int, text: str) -> None:
        self.insert('end', text, f'{font_size}i')

    @__make_writeable
    def write_bold_italic(self, font_size: int, text: str) -> None:
        self.insert('end', text, f'{font_size}bi')


class Tip(Widget, TKLabel):
    @init_widget
    def __init__(self, master: Widget, text: str) -> None:
        self.__text=text
        self.colorize()
        master.bind('<Enter>', self.__show)
        master.bind('<Leave>', self.__hide)

    def colorize(self) -> None:
        self.__bg = Widgeter().theme.aux1,
        self.__fg = Widgeter().theme.fore,

    def __show(self, event) -> None:
        self.__tip: TKToplevel = TKToplevel(bg=self.__bg, bd=0)
        self.__tip.wm_overrideredirect(True)
        self.__tip.geometry(f'+{event.x_root}+{event.y_root}')
        label: TKLabel = TKLabel(master=self.__tip, text=self.__text, bg=self.__bg, fg=self.__fg, justify='left')
        label.pack()

    def __hide(self, event) -> None:
        self.__tip.destroy()


class SpinBox(Widget, TKSpinBox):
    @init_widget
    def __init__(self, master: Widget, from_: int, to: int, command: callable, width: int = 5) -> None:
        TKSpinBox.__init__(
            self,
            master=master,
            from_=from_,
            to=to,
            command=command,
            width=width,
            font=(Widgeter().theme.mono, Widgeter().theme.s, 'bold'),
            justify='center',
            highlightthickness=2,
            bd=0
        )
        self.colorize()

    def colorize(self) -> None:
        self['bg'] = Widgeter().theme.aux1
        self['fg'] = Widgeter().theme.fore
        self['insertbackground'] = Widgeter().theme.aux2
        self['buttonbackground'] = Widgeter().theme.back
        self['highlightbackground'] = Widgeter().theme.aux1
        self['highlightcolor'] = Widgeter().theme.aux2


class Canvas(Widget, TKCanvas):
    def __init__(self, master: Widget, w: int, h: int, path: str) -> None:
        """
        scrap_image = TKPhotoImage(path).resize((w, h))
        scrap_canvas = Canvas(master, bg=Widgeter().theme.back, width=w, height=h, bd=0, highlightthickness=0, relief="flat")
        scrap_canvas.create_image(w / 2, h / 2, image=scrap_image, anchor="center")
        Widget.__init__(self)
        """
        pass


class OptionMenu(Widget, TKOptionMenu):
    def __init__(self, master: Widget, options: list, default: object, command) -> None:
        """    
        self.__var = None
        TKOptionMenu.__init__(self, master, self.__var, *options, default, command=command)
        self.configure(
            bg=Widgeter().theme.back,
            fg=Widgeter().theme.fore,
            activebackground=Widgeter().theme.aux2,
            activeforeground=Widgeter().theme.back,
            relief='flat',
            highlightthickness=0
        )
        self["menu"].config(bg=Widgeter().theme.back, fg=Widgeter().theme.fore, activebackground=Widgeter().theme.aux2, activeforeground=Widgeter().theme.back)
        Widget.__init__(self)
        """
        pass


class Message(Widget, TKMessage):
    def __init__(self, master: Widget, text: str) -> None:
        """
        TKMessage.__init__(master=master, text=text, font=(Widgeter().theme.sans, Widgeter().theme.s), bg=Widgeter().theme.back, fg=Widgeter().theme.fore)
        Widget.__init__(self)
        """
        pass


class ThemeButton(Widget, TKButton):
    @init_widget
    def __init__(self, master: Widget) -> None:
        TKButton.__init__(
            self,
            master=master,
            command=lambda: self.put_next_theme(),
            text=Widgeter().theme.icon,
            font=('Consolas', 30),
            bd=0
        )
        make_pixel_size(button=self, w=30, h=30)
        self.colorize()
        
    def colorize(self) -> None:
        self['bg']=Widgeter().theme.back
        self['fg']=Widgeter().theme.fore
        self['activebackground'] = Widgeter().theme.aux1
        self['activeforeground'] = Widgeter().theme.back
        self['text']= Widgeter().theme.icon

    @classmethod
    def put_next_theme(cls) -> None:
        if len(Widgeter().themes) > 1:

            Widgeter().next_theme()
            
            f = open("error.txt", "w")
            
            counter : int = 0
            try:
                for widget in Widgeter().widgets:
                    counter = counter + 1
                    
                    try:
                        f.write(f'{type(widget)}\n')
                        widget.colorize()
                    except Exception as e:
                        print(f'Error on widget {type(widget)}: {e}')
                    
                    if counter > 100:
                        raise Exception('Loop infinito')
            except Exception as e:
                print(e)

            f.close()

def make_frame_changer(button: Button, from_: Frame, to: Frame) -> None:
    button.configure(command=lambda from_=from_, to=to: (from_.pack_forget(), to.pack(expand=True, fill='both')))


def make_pixel_size(button: Button, w: int, h: int) -> None:
    button.__icon: TKPhotoImage = TKPhotoImage(width=1, height=1)
    button.configure(image=button.__icon, compound="c", width=w, height=h)
