from typing import TypeVar

Widget = TypeVar('Widget')

class Error(Exception):
    def __init__(self, message : str) -> None:
        super().__init__(message)