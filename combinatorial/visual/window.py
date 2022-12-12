from tkinter import StringVar
from combinatorial.visual.widget import Widget
from combinatorial.visual.widget import Root
from combinatorial.visual.widget import Frame
from combinatorial.visual.widget import Label
from combinatorial.visual.widget import Title
from combinatorial.visual.widget import Entry
from combinatorial.visual.widget import Button
from combinatorial.visual.widget import MenuButton
from combinatorial.visual.widget import BackButton
from combinatorial.visual.widget import ThemeButton
from combinatorial.visual.widget import Text
from combinatorial.visual.widget import Tip
from combinatorial.visual.widget import SpinBox
from combinatorial.visual.widget import Message
from combinatorial.visual.output import SymbolicWindow
from combinatorial.project.symbolic_method import Combinatory
from combinatorial import commons

class Window:

    def __new__(self) -> 'Window':
        if not hasattr(self, 'instance'):
            self.instance: 'Window' = super(Window, self).__new__(self)
        return self.instance

    def run(self) -> None:

        self.__root = Root('Combinatorial project', w=500, h=600)

        ' Frames '
        frame: Frame = Frame(master=self.__root)
        frame.pack(side='top', expand=True, fill='both')

        theme_icon = ThemeButton(master=frame)
        theme_icon.pack(side='top', expand=False, anchor='e', padx=20, pady=20)

        subframe: Frame = Frame(master=frame)
        subframe.pack(side='top', expand=True, fill='both')

        menu_frame: Frame = Frame(master=subframe)
        menu_frame.rowconfigure(index=[0, 1, 2, 3], weight=1) # type: ignore
        menu_frame.columnconfigure(index=[0], weight=1) # type: ignore
        menu_frame.pack(expand=True, fill='both',padx=30, pady=30)

        problem_frame: Frame = Frame(master=subframe)

        problems_subframe: Frame = Frame(master=problem_frame)
        problems_subframe.rowconfigure(index=[0, 1, 2, 3], weight=1) # type: ignore
        problems_subframe.columnconfigure(index=[0], weight=1) # type: ignore
        problems_subframe.pack(side='top', expand=True, fill='both')

        symbolic_framework: Frame = Frame(master=subframe)

        symbolic_subframe: Frame = Frame(master=symbolic_framework)
        symbolic_subframe.pack(expand=True, fill='both', padx=20)

        fractal_framework: Frame = Frame(master=subframe)

        fractal_tab_box = Frame(master=fractal_framework, bg='blue')
        fractal_tab_box.rowconfigure(index=[0], weight=1) # type: ignore
        fractal_tab_box.columnconfigure(index=[1], weight=30) # type: ignore
        fractal_tab_box.columnconfigure(index=[0, 2], weight=1) # type: ignore
        fractal_tab_box.pack(anchor='n', expand=True, fill='x')

        fractal_subframe: Frame = Frame(master=fractal_framework)
        fractal_subframe.pack(expand=True, fill='both', padx=20)

        about_frame: Frame = Frame(master=subframe)

        ' Menu '
        menu_title: Title = Title(master=menu_frame, text='Método Simbólico &\nFractales')
        menu_title.grid(column=0, row=0)

        problem_button: MenuButton = MenuButton(master=menu_frame, text='INICIAR', from_=menu_frame, to=problem_frame)
        problem_button.grid(column=0, row=1)

        about_button: MenuButton = MenuButton(master=menu_frame, text='ABOUT', from_=menu_frame, to=about_frame)
        about_button.grid(column=0, row=2)

        ' Problem '
        symbolic_button: MenuButton = MenuButton(master=problems_subframe, text='METODO SIMBOLICO', from_=problem_frame, to=symbolic_framework)
        symbolic_button.grid(column=0, row=1)

        fractal_button: MenuButton = MenuButton(master=problems_subframe, text='FRACTALES', from_=problem_frame, to=fractal_framework)
        fractal_button.grid(column=0, row=2)

        problem_back_button: BackButton = BackButton(master=problem_frame, from_=problem_frame, to=menu_frame)
        problem_back_button.pack(side='top', expand=False, anchor='w')

        ' Symbolic '
        symbolic_back_button: BackButton = BackButton(master=symbolic_framework, from_=symbolic_framework, to=problem_frame)
        symbolic_back_button.pack(side='top', expand=False, anchor='w')

        symbolic_frame: Frame = self.__get_symbolic_frame(master=symbolic_subframe)
        symbolic_frame.pack(expand=True, fill='both')

        ' Fractal '
        #!Test

        ' About '
        about_text: Text = Text(master=about_frame, font_sizes=[15, 25], readonly=True, border=False)
        about_text.write_italic(font_size=25, text='Proyecto computacional:\nEntrega 2\n\n')
        about_text.write_bold(font_size=15, text='Andrea Arias\n')
        about_text.write_bold(font_size=15, text='Omar Cifuentes\n')
        about_text.write_bold(font_size=15, text='Santiago Hernández\n')
        about_text.pack(expand=True, fill='both', padx=30)

        about_back_button: BackButton = BackButton(master=about_frame, from_=about_frame, to=menu_frame)
        about_back_button.pack(expand=False, anchor='w')

        ' Start '
        self.__root.mainloop()
       
    def __get_symbolic_frame(self, master : Widget):
        
        frame = Frame(master=master)
        frame.rowconfigure(index=[0, 1, 2, 3], weight=1) # type: ignore
        frame.columnconfigure(index=[0], weight=1) # type: ignore
        frame.pack(expand=True, fill='both')

        title: Title = Title(master=frame, text='Combinatoria')
        title.grid(row=0, column=0)

        entry_frame: Frame = Frame(master=frame)
        entry_frame.rowconfigure(index=[0, 1, 2, 3], weight=1) # type: ignore
        entry_frame.columnconfigure(index=[0, 1], weight=1) # type: ignore
        entry_frame.grid(row=1, column=0)
        
        base_label: Label = Label(master=entry_frame, text='b:')
        base_label.grid(row=0, column=0, sticky='ew', padx=5)

        base_tip : Tip = Tip(master=base_label, text='Base de caracteres.\nEjemplo: base 2 para cadenas de ceros y unos (0 y 1).')
        
        base_entry: Entry = Entry(master=entry_frame)
        base_entry.grid(row=0, column=1, sticky='w', pady=5, ipady=3)

        size_label: Label = Label(master=entry_frame, text='n:')
        size_label.grid(row=1, column=0, sticky='ew', padx=5)

        size_tip : Tip = Tip(master=size_label, text=f'La cantidad n de caracteres de la cadena.\nEjemplo: n = 4 para {chr(39)}0101{chr(39)}.')

        size_entry: Entry = Entry(master=entry_frame)
        size_entry.grid(row=1, column=1, sticky='w', pady=5, ipady=3)

        bans_label: Label = Label(master=entry_frame, text='e:')
        bans_label.grid(row=2, column=0, sticky='ew', padx=5)

        bans_tip : Tip = Tip(master = bans_label, text = f'Subcadenas excluidas de la combinatoria.\nEjemplo: para una cadena binaria de 2 caracteres exceptuando a {chr(34)}00{chr(34)} se obtendrían 01, 10, 11.')

        bans_spin : SpinBox = SpinBox(master=entry_frame, from_=0,to=10,command=...)
        bans_spin.configure(command=...)
        bans_spin.grid(row=2, column=1, sticky='ew', padx=5)

        button: Button = Button(master=frame, text='Calcular', command=...)
        button.bd = 'red'
        button.grid(row=3, column=0)

        return frame