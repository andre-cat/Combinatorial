from tkinter import Widget as tkWidget
from tkinter import Frame as tkFrame
from tkinter import Label as tkLabel
from tkinter import Entry as tkEntry
from tkinter import Text as tkText
from tkinter import Button as tkButton
from tkinter import Canvas as tkCanvas
from tkinter import messagebox as tkMessagebox
from tkinter import PhotoImage as tkPhotoImage
from tkinter.ttk import Notebook as ttNotebook
from tkinter.ttk import Combobox as ttCombobox
from tkinter.tix import Tk as txTk
from tkinter.tix import TixWidget as txWidget
from tkinter.tix import Balloon as txBalloon
from typing import Callable
import re as regex
import sys
from combinatorial import commons
from combinatorial.visual.widgeter import Widgeter
from combinatorial.visual.theme import Theme
from combinatorial.visual.output import SymbolicWindow
from combinatorial.project.symbolic_method import Combinatory
from combinatorial.project.fractal import Fractal


class Window():

    def __new__(cls) -> 'Window':
        if not hasattr(cls, 'instance'):
            cls.__instance: 'Window' = super(Window, cls).__new__(cls)
            cls.__window : txTk = txTk()

            b: int = 500
            h: int = 600
            x: int = (int)(cls.__window.winfo_screenwidth() / 2 - b / 2)
            y: int = (int)(cls.__window.winfo_screenheight() / 2 - h / 2)
            cls.__window.geometry(f'{b}x{h}+{x}+{y}')
            cls.__window.title('PyScraper')
            cls.__window['bg'] = 'white'
            cls.__window.resizable(True, True)

            white_theme = Theme()
            black_theme = Theme(back='black', fore='white', aux1='SlateGrey', aux2='#ededed', anot='red', icon='☾')

            themes: list[Theme] = [white_theme, black_theme]

            cls.__widgeter = Widgeter(window=cls.__window, themes=themes)

        return cls.__instance

    @classmethod
    def run(cls) -> None:

        " Frames "
        frame: tkFrame = tkFrame(master=cls.__window, bg=cls.__widgeter.theme.back)
        frame.pack(side='top', expand=True, fill='both')
        cls.__widgeter.widgets.append(frame)
        
        cls.__widgeter.put_icon_theme(master=frame)

        subframe: tkFrame = cls.__widgeter.frame(master=frame)
        subframe.pack(side='top', expand=True, fill='both')

        menu_frame: tkFrame = cls.__widgeter.frame(master=subframe)
        menu_frame.rowconfigure(index=[0, 1, 2, 3], weight=1) # type: ignore
        menu_frame.columnconfigure(index=[0], weight=1) # type: ignore
        menu_frame.pack(expand=True, fill='both')

        problem_frame: tkFrame = cls.__widgeter.frame(master=subframe)

        problems_subframe: tkFrame = cls.__widgeter.frame(master=problem_frame)
        problems_subframe.rowconfigure(index=[0, 1, 2, 3], weight=1) # type: ignore
        problems_subframe.columnconfigure(index=[0], weight=1) # type: ignore
        problems_subframe.pack(side='top', expand=True, fill='both')

        symbolic_framework: tkFrame = cls.__widgeter.frame(master=subframe)

        symbolic_subframe: tkFrame = cls.__widgeter.frame(master=symbolic_framework)
        symbolic_subframe.pack(expand=True, fill='both', padx=20)

        fractal_framework: tkFrame = cls.__widgeter.frame(master=subframe)

        fractal_tab_box = tkFrame(master=fractal_framework, bg='blue',height=20)
        fractal_tab_box.rowconfigure(index=[0], weight=1) # type: ignore
        fractal_tab_box.columnconfigure(index=[1], weight=30) # type: ignore
        fractal_tab_box.columnconfigure(index=[0,2], weight=1) # type: ignore
        fractal_tab_box.pack(anchor='n',expand=True, fill='x')

        fractal_subframe: tkFrame = cls.__widgeter.frame(master=fractal_framework)
        fractal_subframe.pack(expand=True, fill='both', padx=20)

        about_frame: tkFrame = cls.__widgeter.frame(master=subframe)

        " Menu "
        menu_title: tkLabel = cls.__widgeter.title(master=menu_frame, text='Método Simbólico &\nFractales')
        menu_title.grid(column=0, row=0)

        problem_button: tkButton = cls.__widgeter.menu_button(master=menu_frame, text='INICIAR', ini=menu_frame, end=problem_frame)
        problem_button.grid(column=0, row=1)

        about_button: tkButton = cls.__widgeter.menu_button(master=menu_frame, text='ABOUT', ini=menu_frame, end=about_frame)
        about_button.grid(column=0, row=2)

        " Problem "
        symbolic_button: tkButton = cls.__widgeter.menu_button(master=problems_subframe, text='METODO SIMBOLICO', ini=problem_frame, end=symbolic_framework)
        symbolic_button.grid(column=0, row=1)

        fractal_button: tkButton = cls.__widgeter.menu_button(master=problems_subframe, text='FRACTALES', ini=problem_frame, end=fractal_framework)
        fractal_button.grid(column=0, row=2)

        problem_back_button: tkButton = cls.__widgeter.back_button(master=problem_frame, ini=problem_frame, end=menu_frame)
        problem_back_button.pack(side='top', expand=False, anchor='w')

        " Symbolic "
        symbolic_back_button: tkButton = cls.__widgeter.back_button(master=symbolic_framework, ini=symbolic_framework, end=problem_frame)
        symbolic_back_button.pack(side='top', expand=False, anchor='w')

        symbolic_frame = Window.__symbolic_frame(symbolic_subframe)
        symbolic_frame.pack(expand=True, fill='both')

        " Fractal "
        fractal_back_button: tkButton = cls.__widgeter.back_button(master=fractal_framework, ini=fractal_framework, end=problem_frame)
        fractal_back_button.pack(side='top', expand=False, anchor='w')

        box1 = cls.__widgeter.button(master=fractal_tab_box, command=lambda:print('a'),font_size=8)
        box1.grid(row=0,column=0,sticky='nsew')
        box1.configure(bd = 0)

        box2 = tkFrame(master=fractal_tab_box, bg='orange',height=20)
        box2.grid(row=0,column=1,sticky='nsew')

        box3 = cls.__widgeter.button(master=fractal_tab_box, command=lambda:print('b'),font_size=8)
        box3.grid(row=0,column=2,sticky='nsew')
        box3.configure(bd = 0)
        
        #box1.pack(anchor='nw',expand=False)
        #box2.pack(anchor='nw',expand=True, fill='x')
        #box3.pack(anchor='nw',expand=False)

        """
        fractal_book: ttNotebook = ttNotebook(master=fractal_subframe)
        fractal_book.pack(expand=True, fill='both')
        
        fractal_tab_1 : tkFrame = cls.__fractal_frame(parent=fractal_book,title='A',photo_path='sierpinski_carpet.png',function=Fractal.sierpinski_carpet)

        fractal_book.add(fractal_tab_1, text='Sierpinski Carpet')
        #fractal_book.add(fractal_2, text='Sierpinski Sieve (60)')
        #fractal_book.add(fractal_3, text='Sierpinski Sieve (90)')
        #fractal_book.add(fractal_4, text='Sierpinski Sieve (102)')
        #fractal_book.add(fractal_5, text='H')
        #fractal_book.add(fractal_6, text='Haferman Carpet')
        #fractal_book.add(fractal_7, text='Cantor Square')
        #fractal_book.add(fractal_8, text='Box')
        """

        " About "
        about_text: tkText = cls.__widgeter.text(master=about_frame)
        about_text.tag_config('title', font=('Times New Roman', 30))
        about_text.tag_config('fonts', font=('Times New Roman', 20))
        about_text.insert('end', 'Proyecto computacional:\nEntrega 2\n\n', 'title')
        about_text.insert('end', 'Andrea Arias\n', 'fonts')
        about_text.insert('end', 'Omar Cifuentes\n', 'fonts')
        about_text.insert('end', 'Santiago Hernández\n', 'fonts')
        about_text.configure(state='disabled')
        about_text.pack(expand=True, fill='both', padx=40)

        about_back_button: tkButton = cls.__widgeter.back_button(master=about_frame, ini=about_frame, end=menu_frame)
        about_back_button.pack(expand=False, anchor='w')

        " Start "
        cls.__window.mainloop()

    @classmethod
    def __symbolic_frame(cls, parent: tkWidget) -> tkFrame:
        frame: tkFrame = cls.__widgeter.frame(parent)
        frame.rowconfigure(index=[0,1,2,3], weight=1)  # type: ignore
        frame.columnconfigure(index=[0], weight=1)  # type: ignore
        frame.pack(expand=True, fill='both')

        title: tkLabel = cls.__widgeter.title(master=frame, text='Combinatoria')
        title.grid(row=0, column=0)

        entry_frame = cls.__widgeter.frame(master=frame)
        entry_frame.rowconfigure(index=[0, 1, 2,3], weight=1)  # type: ignore
        entry_frame.columnconfigure(index=[0, 1], weight=1)  # type: ignore
        entry_frame.grid(row=1, column=0)

        base_label: tkLabel = cls.__widgeter.label(master=entry_frame, text='Base:')
        base_label.grid(row=0, column=0, sticky='ew', padx=5)

        base_balloon = txBalloon(master=parent)
        base_balloon.bind_widget(base_label, balloonmsg='Base de caracteres.\nEjemplo: base 2 para cadenas de ceros y unos (0 y 1).')

        base_entry: tkEntry = cls.__widgeter.entry(master=entry_frame)
        base_entry.grid(row=0, column=1, sticky='w', pady=5, ipady=3)

        size_label: tkLabel = cls.__widgeter.label(master=entry_frame, text='n:')
        size_label.grid(row=1, column=0, sticky='ew', padx=5)

        size_balloon = txBalloon(master=parent)
        size_balloon.bind_widget(size_label, balloonmsg=f"La cantidad n de caracteres de la cadena.\nEjemplo: n = 4 para {chr(39)}0101{chr(39)}")

        size_entry: tkEntry = cls.__widgeter.entry(master=entry_frame)
        size_entry.grid(row=1, column=1, sticky='w', pady=5, ipady=3)

        bans_label: tkLabel = cls.__widgeter.label(master=entry_frame, text='Exc:')
        bans_label.grid(row=2, column=0, sticky='ew', padx=5)

        bans_balloon = txBalloon(master=frame)
        bans_balloon.bind_widget(bans_label, balloonmsg=f'Subcadenas excluidas de la combinatoria.\nEjemplo: para una cadena binaria de 2 caracteres exceptuando a {chr(34)}00{chr(34)} se obtendrían 01, 10, 11.')

        bans_combo: ttCombobox = ttCombobox(master=entry_frame, state='readonly', values=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], font=('Dubai', 13), justify='center', width=4)
        bans_combo.current(0)
        bans_combo.grid(row=2, column=1, pady=5, ipady=3)

        bans_frame: tkFrame = cls.__widgeter.frame(master=frame)
        bans_frame.grid(row=2, column=0,sticky='nsew')

        bans_combo.bind('<<ComboboxSelected>>',  lambda event, combo=bans_combo, frame=bans_frame: cls.__create_box(event, combo, frame)) # type: ignore

        button: tkButton = cls.__widgeter.button(master=frame, command=lambda:Window.__run_symbolic(base_entry, size_entry, bans_frame), text='Calcular')
        button.configure(font=('Consolas', 12, 'bold'))
        button.grid(row=3, column=0)

        return frame

    @classmethod
    def __create_box(cls, event: Callable, combobox: ttCombobox, frame: tkFrame) -> None:
        if Window.__val_combo(combobox):
            if len(frame.winfo_children()) > 0:
                cls.__widgeter.widgets.remove(frame.winfo_children()[0])
                frame.winfo_children()[0].destroy()

            sub_frame = cls.__widgeter.frame(master=frame)
            sub_frame.pack()

            sub_frame.rowconfigure(index=[0], weight=1)  # type: ignore
            for index in range(int(combobox.current())):
                sub_frame.columnconfigure(index=index)  # type: ignore

                entry = cls.__widgeter.entry(master=sub_frame, width=4)
                entry.insert(0, '')
                entry.grid(row=0, column=index, padx=10, ipady=5,sticky='ns')

    @classmethod
    def __run_symbolic(cls, base_entry : tkEntry, size_entry:tkEntry, bans_frame:tkFrame) -> None:
        try:
            if Window.__is_empty(base_entry.get()):
                raise commons.Error('Debe insertar un número de base.')
            elif not Window.__is_number(base_entry.get()):
                raise commons.Error('Debe insertar un número válido para base.')
            
            if Window.__is_empty(size_entry.get()):
                raise commons.Error('Debe insertar un número de tamaño.')
            elif not Window.__is_number(size_entry.get()):
                raise commons.Error('Debe insertar un número válido para tamaño.')

            bans : list[str] = [] 
            if len(bans_frame.winfo_children()) > 0:
                if len(bans_frame.winfo_children()[0].winfo_children()) > 0:

                    for wid in bans_frame.winfo_children()[0].winfo_children():
                        if type(wid) == tkEntry:                    
                            if Window.__is_empty(wid.get()):
                                bans.append(wid.get())
                            else:
                                raise commons.Error('Debe llenar todas las casillas de exclusión.')

            combinatory : Combinatory = Combinatory(base=int(base_entry.get()),size=int(size_entry.get()),bans=bans)
        
            symbolic_window = SymbolicWindow(combinatory=combinatory, theme=cls.__widgeter.theme)
        except commons.Error as e:
            tkMessagebox.showerror('Error!', str(e))
        except Exception as e:
            print(f'{__file__}:\n{str(e)}\n{sys.exc_info()[-1].tb_lineno}') # type: ignore

    @classmethod
    def __fractal_frame(cls, parent: tkWidget, title: str, photo_path: str, function: Callable) -> tkFrame:
        frame: tkFrame = cls.__widgeter.frame(parent)
        frame.rowconfigure(index=[0, 1, 2], weight=1)  # type: ignore
        frame.columnconfigure(index=[0, 1], weight=1)  # type: ignore
        frame.pack(expand=True, fill='both')

        __title: tkLabel = cls.__widgeter.title(master=frame, text=title)
        __title.grid(column=0, row=0)

        frame_entry = cls.__widgeter.frame(master=frame)
        frame_entry.grid(column=0, row=1)

        #photo = PhotoImage(file = constants.PATH + f'/resources/images/{photo_path}')

        #canvas = Canvas(frame, bg=frame['bg'], width=photo.width(), height=photo.height(), bd=0, highlightthickness=0, relief="flat")
        #canvas.create_image(photo.width() / 2, photo.height() / 2, image=photo, anchor="center")
        #canvas.grid(row=1, column=0)

        label: tkLabel = cls.__widgeter.label(master=frame_entry, text=f'Inserte n (iteraciones): ')
        label.pack()

        entry: tkEntry = cls.__widgeter.entry(master=frame_entry)
        entry.pack(pady=4, ipadx=3, ipady=3)

        button: tkButton = cls.__widgeter.button(master=frame, command=lambda: print(function, entry.get()), text='Calcular')
        button.configure(font=('Consolas', 12, 'bold'))
        button.grid(column=0, row=2)

        return frame

    @staticmethod
    def __val_combo(combobox: ttCombobox) -> bool:
        return combobox.current() != -1

    @staticmethod
    def __is_number(string: str) -> bool:
        return regex.match('^\d*$', string)

    def __is_empty(string: str) -> bool:
        return len(string) == 0
