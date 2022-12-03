from typing import Optional


class Theme:

    def __init__(
        self,
        back: str = 'white',
        fore: str = 'black',
        aux1: str = '#ededed',
        aux2: str = 'SlateGray',
        anot: str = 'lime',
        icon: str = '☀',
        sans: str = 'Lucida Sans',
        mono: str = 'Consolas',
        seri: str = 'OCR A Extended') -> None:
        
        self.__back: str = back
        self.__fore: str = fore
        self.__aux1: str = aux1
        self.__aux2: str = aux2
        self.__anot: str = anot
        self.__icon = icon
        self.__sans = sans
        self.__mono = mono
        self.__seri = seri

    @property
    def back(self):
        return self.__back

    @property
    def fore(self):
        return self.__fore

    @property
    def aux1(self):
        return self.__aux1

    @property
    def aux2(self):
        return self.__aux2

    @property
    def anot(self):
        return self.__anot

    @property
    def sans(self):
        return self.__sans

    @property
    def mono(self):
        return self.__mono

    @property
    def seri(self):
        return self.__seri

    @property
    def icon(self):
        return self.__icon
