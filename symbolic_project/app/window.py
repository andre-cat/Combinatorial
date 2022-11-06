from tkinter import Tk
from tkinter import Widget
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import PhotoImage
from tkinter import Entry
from tkinter import Text
from tkinter import Canvas
from tkinter import messagebox as Messagebox
from tkinter.ttk import Style as TStyle
from tkinter.ttk import Notebook as TNotebook
from tkinter.ttk import Combobox as TCombobox
from symbolic_project.constants import PATH
from symbolic_project.project import fractal
from symbolic_project.project import symbolic_method

__back_color = 'white'
__fore_color = 'black'
__theme_button: Button
__style: TStyle
__moon_icon: PhotoImage
__widgets: list
__options_1 : TCombobox
__options_2 : TCombobox

def run():
    global __widgets
    __widgets = []

    window = Tk()
    __widgets.append(window)

    b: int = 600
    h: int = 500
    x: int = (int)(window.winfo_screenwidth() / 2 - b / 2)
    y: int = (int)(window.winfo_screenheight() / 2 - h / 2)

    window.title('PyScraper')
    window['bg'] = __back_color
    window.resizable(True, True)
    window.geometry(f'{b}x{h}+{x}+{y}')

    global __style
    __style = TStyle(window)
    __style.theme_create("white",
                         parent="alt",
                         settings={
                             "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0], "background": 'white'}},
                             "TNotebook.Tab": {
                                 "configure": {"padding": [7, 2], "background": '#ededed', "foreground": 'black', 'font': ('Century Gothic', 11)},
                                 "map":       {"background": [("selected", 'white')], 'foreground': [("selected", 'black')], "expand": [("selected", [1, 1, 1, 0])]}}})

    __style.theme_create("black",
                         parent="alt",
                         settings={
                             "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0], "background": 'black'}},
                             "TNotebook.Tab": {
                                 "configure": {"padding": [7, 2], "background": 'grey', "foreground": 'white', 'font': ('Century Gothic', 11)},
                                 "map":       {"background": [("selected", 'black')], 'foreground': [("selected", 'white')], "expand": [("selected", [1, 1, 1, 0])]}}})

    toggle_bar()

    global __theme_button
    __theme_button = Button(master=window, command=lambda: __change_theme(), border=0)
    __theme_button.pack(side='top', expand=False, anchor='e', padx=10, pady=10)
    toggle_icon()

    frame: Frame = __frame(parent=window)
    frame.pack(side='top', expand=True, fill='both')
    __widgets.append(frame)

    # Menus
    menu_frame: Frame = __frame(parent=frame)
    menu_frame.rowconfigure(index=[0, 1, 2, 3], weight=1)
    menu_frame.columnconfigure(index=[0], weight=1)
    menu_frame.pack(expand=True, fill='both')
    __widgets.append(menu_frame)

    problem_frame: Frame = __frame(parent=frame)
    __widgets.append(problem_frame)

    problems_subframe: Frame = __frame(parent=problem_frame)
    problems_subframe.rowconfigure(index=[0, 1, 2, 3], weight=1)
    problems_subframe.columnconfigure(index=[0], weight=1)
    problems_subframe.pack(side='top', expand=True, fill='both')
    __widgets.append(problems_subframe)

    symbolic_frame: Frame = __frame(parent=frame)
    __widgets.append(symbolic_frame)

    symbolic_book: TNotebook = TNotebook(master=symbolic_frame)
    symbolic_book.pack(expand=True, fill='both')
    __widgets.append(symbolic_book)

    symbolic_1_list = ['Cadenas binarias de tamaño n sin subcadenas 00 y 11', 'Cadenas ternarias de tamaño n sin la subcadena 00', 'Cadenas cuaternarias de tamaño n con caracteres en orden creciente', 'Cadenas ternarias de tamaño n sin la subcadena 22', 'Cadenas ternarias sin la subcadena 22']
    symbolic_1: Frame = __symbolic_frame(parent=symbolic_book, title="Metodo simbólico: Parte 1", options=symbolic_1_list)
    symbolic_1.pack(expand=True, fill='both')
    __widgets.append(symbolic_1)

    symbolic_2: Frame = __frame(parent=symbolic_book)
    symbolic_2.pack(expand=True, fill='both')
    __widgets.append(symbolic_2)

    symbolic_book.add(symbolic_1, text='Parte 1')
    symbolic_book.add(symbolic_2, text='Parte 2')

    fractal_frame: Frame = __frame(parent=frame)
    __widgets.append(fractal_frame)

    fractal_book: TNotebook = TNotebook(master=fractal_frame)
    fractal_book.pack(expand=True, fill='both')
    __widgets.append(fractal_book)

    fractal_1: Frame = __fractal_frame(parent=fractal_book, title="Sierpinski Carpe", function=fractal.sierpinski_carpet)
    fractal_1.pack(expand=True, fill='both')

    fractal_2: Frame = __fractal_frame(parent=fractal_book, title="Sierpinski Sieve (60)", function=lambda: fractal.sierpinsky_sieve_60)
    fractal_2.pack(expand=True, fill='both')

    fractal_3: Frame = __fractal_frame(parent=fractal_book, title="Sierpinski Sieve (90)", function=lambda: fractal.sierpinsky_sieve_90)
    fractal_3.pack(expand=True, fill='both')

    fractal_4: Frame = __fractal_frame(parent=fractal_book, title="Sierpinski Sieve (102)", function=lambda: fractal.sierpinsky_sieve_102)
    fractal_4.pack(expand=True, fill='both')

    fractal_5: Frame = __fractal_frame(parent=fractal_book, title='H', function=lambda: fractal.h)
    fractal_5.pack(expand=True, fill='both')

    fractal_6: Frame = __fractal_frame(parent=fractal_book, title="Haferman Carpet", function=lambda: fractal.haferman_carpet)
    fractal_6.pack(expand=True, fill='both')

    fractal_7: Frame = __fractal_frame(parent=fractal_book, title="Cantor Square", function=lambda: fractal.cantor_square)
    fractal_7.pack(expand=True, fill='both')

    fractal_8: Frame = __fractal_frame(parent=fractal_book, title="Box", function=lambda: fractal.box)
    fractal_8.pack(expand=True, fill='both')

    fractal_book.add(fractal_1, text='Sierpinski Carpet')
    fractal_book.add(fractal_2, text='Sierpinski Sieve (60)')
    fractal_book.add(fractal_3, text='Sierpinski Sieve (90)')
    fractal_book.add(fractal_4, text='Sierpinski Sieve (102)')
    fractal_book.add(fractal_5, text='H')
    fractal_book.add(fractal_6, text='Haferman Carpet')
    fractal_book.add(fractal_7, text='Cantor Square')
    fractal_book.add(fractal_8, text='Box')

    about_frame: Frame = __frame(parent=frame)
    # __widgets.append(about_frame)

    # Main menu
    menu_title: Label = __title_label(parent=menu_frame, text='Metodo Simbólico &\nFractales')
    menu_title.grid(column=0, row=0)

    problem_button: Button = __menu_button(parent=menu_frame, text='INICIAR', command=lambda: __go_to(problem_frame, menu_frame))
    problem_button.grid(column=0, row=1)

    about_button: Button = __menu_button(parent=menu_frame, text='ABOUT', command=lambda: __go_to(about_frame, menu_frame))
    about_button.grid(column=0, row=2)

    # Problem Menu
    symbolic_button: Button = __menu_button(parent=problems_subframe, text='METODO SIMBOLICO', command=lambda: __go_to(symbolic_frame, problem_frame))
    symbolic_button.grid(column=0, row=1)

    fractal_button: Button = __menu_button(parent=problems_subframe, text='FRACTALES', command=lambda: __go_to(fractal_frame, problem_frame))
    fractal_button.grid(column=0, row=2)

    problem_back_button: Button = __back_button(parent=problem_frame, command=lambda: __go_to(menu_frame, problem_frame))
    problem_back_button.pack(side='top', expand=False, anchor='w')

    # Symbolic Menu
    symbolic_back_button: Button = __back_button(parent=symbolic_frame, command=lambda: __go_to(problem_frame, symbolic_frame))
    symbolic_back_button.pack(side='top', expand=False, anchor='w')

    # Fractal Menu
    fractal_back_button: Button = __back_button(parent=fractal_frame, command=lambda: __go_to(problem_frame, fractal_frame))
    fractal_back_button.pack(side='top', expand=False, anchor='w')

    # About Menu
    about_text: Text = Text(master=about_frame, wrap="word", highlightthickness=0, border=0)
    about_text.tag_config("title", font=("Times New Roman", 30))
    about_text.tag_config("fonts", font=("Times New Roman", 20))
    about_text.insert("end", "Proyecto computacional:\nEntrega 2\n\n", 'title')
    about_text.insert("end", "Andrea Arias\n", 'fonts')
    about_text.insert("end", "Omar Cifuentes\n", 'fonts')
    about_text.insert("end", "Santiago Hernández\n", 'fonts')
    about_text.configure(state="disabled")
    about_text.pack(expand=True, fill='both', padx=40)

    about_back_button: Button = __back_button(parent=about_frame, command=lambda: __go_to(menu_frame, about_frame))
    about_back_button.pack(expand=False, anchor='w')

    window.mainloop()


def __change_theme() -> None:
    global __widgets
    global __back_color
    global __fore_color
    global __moon_icon

    __back_color, __fore_color = __fore_color, __back_color

    for widget in __widgets:
        try:
            widget.configure(bg=__back_color)  # type: ignore
        except (Exception):
            pass

        try:
            widget.configure(fg=__fore_color)  # type: ignore
        except (Exception):
            pass

    toggle_bar()
    toggle_icon()


def __frame(parent: Widget) -> Frame:
    frame: Frame = Frame(master=parent, bg=__back_color)
    __widgets.append(frame)
    return frame


def __label(parent: Widget, text: str) -> Label:
    label: label = Label(master=parent, bg=__back_color, fg=__fore_color, font=('Corbel', 15), anchor='w', text=text)
    __widgets.append(label)
    return label


def __title_label(parent: Widget, text: str) -> Label:
    label: Label = Label(master=parent, bg=__back_color, fg=__fore_color, font=('Lucida Sans Typewriter', 30), anchor='center', text=text)
    __widgets.append(label)
    return label


def __button(parent: Widget, text: str, command: callable) -> Button:
    button: Button = Button(master=parent, bg=__back_color, fg=__fore_color, text=text, command=command)
    __widgets.append(button)
    return button


def __menu_button(parent: Widget, text: str, command: callable) -> Button:
    button: Button = Button(master=parent, bg=__back_color, fg=__fore_color, font=('Lucida Sans', 18), text=text, command=command)
    __widgets.append(button)
    return button


def __back_button(parent: Widget, command: callable) -> Button:
    button: Button = Button(master=parent, bg=__back_color, fg=__fore_color, font=('Consolas', 14, 'bold'), text='<-', command=command)
    __widgets.append(button)
    return button


def __entry(parent: Widget) -> Entry:
    entry: Entry = Entry(master=parent, bg=__back_color, fg=__fore_color, font=('Consolas', 14), justify="center", border=1, insertbackground="grey", selectbackground='grey', selectforeground='white')
    __widgets.append(entry)
    return entry


def toggle_icon() -> None:
    global __moon_icon
    global __theme_button

    __moon_icon = PhotoImage(file=PATH + f'/resources/images/{__fore_color}_moon.png').zoom(1).subsample(8)
    __theme_button.configure(bg=__back_color, activebackground=__fore_color, image=__moon_icon)


def toggle_bar() -> None:
    global __style
    __style.theme_use(__back_color)


def __go_to(target_frame: Frame, forget_frame: Frame) -> None:
    forget_frame.pack_forget()
    target_frame.pack(expand=True, fill='both')


def __symbolic_frame(parent: Widget, title: str, options: list) -> Frame:
    frame: Frame = __frame(parent)
    frame.rowconfigure(index=[0, 1, 2, 3], weight=1)
    frame.columnconfigure(index=[0], weight=1)
    frame.pack(expand=True, fill='both')

    title: Label = __title_label(parent=frame, text="Metodo simbolico: Parte 1")
    title.grid(column=0, row=0)

    combo_frame: Frame = __frame(parent=frame)
    combo_frame.grid(column=0, row=1, sticky='ew', padx=70)

    label: Label = __label(parent=combo_frame, text="Elija una de las siguientes cadenas:")
    label.pack()

    combo: TCombobox = TCombobox(master=combo_frame, state="readonly", values=options, font=("Dubai", 10), justify='center', width=100)
    combo.bind('<<ComboboxSelected>>',option_changed)
    combo.pack(expand='false', pady=10)

    frame_entry = __frame(parent=frame)
    frame_entry.grid(column=0, row=2)

    label: Label = __label(parent=frame_entry, text=f"Inserte el tamaño de n para las cadenas: ")
    label.pack()

    entry: Entry = __entry(parent=frame_entry)
    entry.pack(pady=4, ipadx=3, ipady=3)

    button: Button = __button(parent=frame, command=lambda: execute(print, ), text='Calcular')
    button.configure(font=('Consolas', 12, 'bold'))
    button.grid(column=0, row=3)

    return frame


def __fractal_frame(parent: Widget, title: str, function: callable) -> Frame:
    frame: Frame = __frame(parent)
    frame.rowconfigure(index=[0, 1, 2], weight=1)
    frame.columnconfigure(index=[0], weight=1)
    frame.pack(expand=True, fill='both')

    title: Label = __title_label(parent=frame, text=title)
    title.grid(column=0, row=0)

    frame_entry = __frame(parent=frame)
    frame_entry.grid(column=0, row=1)

    label: Label = __label(parent=frame_entry, text=f"Inserte el tamaño de n para generar el fractal: ")
    label.pack()

    entry: Entry = __entry(parent=frame_entry)
    entry.pack(pady=4, ipadx=3, ipady=3)

    button: Button = __button(parent=frame, command=lambda: execute(function, entry.get()), text='Calcular')
    button.configure(font=('Consolas', 12, 'bold'))
    button.grid(column=0, row=2)

    return frame


def execute(function: callable, *arguments):
    try:
        int(*arguments)
        function(*arguments)
    except:
        Messagebox.showerror("ERROR!", "Debe insertar un entero.")

def option_changed(event):
    option : str = *args.get()
    if option.__contains__('n'):
        #print('enabled')
        entry.configure(estate='disabled')
        print('enabled')
    else:
        print('disabled')
        entry.configure(estate='enabled')
    