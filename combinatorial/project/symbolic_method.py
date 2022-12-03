from typing import Callable
import sys


class Combinatory:

    def __init__(self, base: int = 0, size: int = 0, bans: list[str] = []):
            self.__base: int = base
            self.__size: int = size
            self.__bans: list[str] = bans
            self.generate : Callable[[], list[str]] = self.generate_from_instance

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, base: int):
        self.__base = base

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def bans(self):
        return self.__bans

    @bans.setter
    def bans(self, bans: list[str]):
        self.__bans = bans
    
    def generate(base: int, size: int, bans: list[str]) -> list[str]:
        strings: list[str] = []
        chars = [None] * size
        Combinatory.__generate(strings, base, size, bans, chars, 0)
        return strings

    def generate_from_instance(self) -> list[str]:
        return Combinatory.generate(self.__base, self.__size, self.__bans)

    @staticmethod
    def __generate(strings: list[str], base: int, size: int, bans: list, chars: list, index: int) -> None:

        try:
            if index < len(chars):
                for char in range(0, base):
                    chars[index] = char
                    Combinatory.__generate(strings, base, size, bans, chars, index + 1)
            else:
                string: str = ''
                for index in range(0, size):
                    string = f'{string}{chars[index]}'

                excluded_string: bool = False
                try:
                    for exclution in bans:
                        if string.__contains__(exclution):
                            raise Exception
                except (Exception):
                    excluded_string = True

                if not (excluded_string):
                    strings.append(string)

        except Exception as e:
            print(f'{__file__}:\n{str(e)}\n{sys.exc_info()[-1].tb_lineno}') # type: ignore
