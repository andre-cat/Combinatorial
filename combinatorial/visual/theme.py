from typing import Optional


class Theme:

    __sans: str = 'Lucida Sans'
    __mono: str = 'Consolas'
    __seri: str = 'OCR A Extended'
    __s: int = 15
    __m: int = 20
    __l: int = 30 


    @property
    def sans(cls):
        return cls.__sans

    @property
    def mono(cls):
        return cls.__mono

    @property
    def seri(cls):
        return cls.__seri
    
    @property
    def s(cls):
        return cls.__s
    
    @property
    def m(cls):
        return cls.__m

    @property
    def l(cls):
        return cls.__l
    

    def __init__(self, back: str = 'white', fore: str = 'black', aux1: str = '#ededed', aux2: str = 'lime', icon: str = '\U00002600') -> None:

        self.__back: str = back
        self.__fore: str = fore
        self.__aux1: str = aux1
        self.__aux2: str = aux2
        self.__icon = icon

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
    def icon(self):
        return self.__icon