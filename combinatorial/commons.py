import re as regex

class String:
    
    def is_number(string: str) -> bool:
        return regex.match('^\d*$', string)

    def is_empty(string: str) -> bool:
        return len(string) == 0

class Error(Exception):
    def __init__(self, message : str) -> None:
        super().__init__(message)