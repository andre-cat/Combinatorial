from tkinter import Tk as tkTk
from tkinter import Frame as tkFrame
from tkinter import Label as tkLabel
from tkinter.scrolledtext import ScrolledText as tkScrolledText
import sys
from combinatorial.project.symbolic_method import Combinatory 
from combinatorial.visual.theme import Theme

class SymbolicWindow:
    def __init__(self, combinatory : Combinatory = Combinatory()):
        try:
            window = tkTk();

            b: int = 350
            h: int = 400
            x: int = (int)(window.winfo_screenwidth() / 2 - b / 2)
            y: int = (int)(window.winfo_screenheight() / 2 - h / 2)

            window.title(f'Symbolic Window B{combinatory.base}N{combinatory.size}E{chr(32).join(combinatory.bans)}')
            #window['bg'] = theme.back
            window.resizable(True, True)
            window.geometry(f'{b}x{h}+{x}+{y}')
            
            frame = tkFrame(master = window)
            frame.pack(fill='both', expand=True, pady=30)

            subframe = tkFrame(master = frame)
            subframe.pack(fill='both', expand=True,padx=20)
            
            box = tkFrame(master=subframe)
            box.rowconfigure(index=[0, 1, 2], weight=1)  # type: ignore
            box.columnconfigure(index=[0], weight=1)  # type: ignore
            box.pack(fill='both', expand=True, pady=20)

            base_label: tkLabel = tkLabel(master=box, font=('Lucida Console',14,'italic'),text=f'Base: {combinatory.base}', anchor='w')
            base_label.grid(row=0, column=0, sticky='ew', pady=5)

            size_label: tkLabel = tkLabel(master=box, font=('Lucida Console',14,'italic'), text=f'Tamaño: {combinatory.size}', anchor='w')
            size_label.grid(row=1, column=0, sticky='ew', pady=5)

            bans_label: tkLabel = tkLabel(master=box, font=('Lucida Console',14,'italic'), text=f'Exclusiones: {chr(44).join(combinatory.bans)}', anchor='w')
            bans_label.grid(row=2, column=0, sticky='ew', pady=5)

            strings = combinatory.generate()
            scrolledtext = tkScrolledText(master=subframe, font=("Consolas", 15, 'bold'), state='normal', wrap='word', highlightthickness=0, bd=0)
            scrolledtext.configure(state='normal')
            scrolledtext.insert('insert', chr(10).join(strings))
            scrolledtext.configure(state='disabled')
            scrolledtext.pack(fill='both', expand=True, ipadx=10,ipady=10)

        except Exception as e:
            print(f'{__file__}:\n{str(e)}\n{sys.exc_info()[-1].tb_lineno}') # type: ignore