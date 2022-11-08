from symbolic_project.project.symbolic_method.combinatory import Combinatory # type: ignore
from symbolic_project.project.symbolic_method import functions # type: ignore
from typing import Optional

class SymbolicWindow:
    def __init__(self, code : str):
        base = int(code[0])
        amount = code[1]
        length = int(code[2])
        exclutions = code[code.find('E[')+2:code.find(']')].split(',')
        exclutions = exclutions if exclutions != [''] else []

        self.__combinatory = Combinatory(base,amount,length,exclutions)
        self.__function = functions.get_function(self.__combinatory)

        
