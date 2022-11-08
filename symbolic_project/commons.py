from os import path
from typing import Final

# CONSTANTS
PATH: Final[str] = path.dirname(path.dirname(__file__))  # Path of project

class Error(Exception):
    def __init__(self,*arguments):
        super(*arguments)