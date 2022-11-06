def generate(base: int, length: int, exclutions: list):
    strings: list = []
    chars = [None] * length
    __generate(strings, base, length, exclutions, chars, 0)
    return strings;

def __generate(strings : list, base: int, length: int, exclutions: list, chars: list, index: int):

    if index < len(chars):
        for char in range(0, base):
            chars[index] = char
            __generate(strings, base, length, exclutions, chars, index + 1)
    else:
        string: str = ''
        for index in range(0, length):
            string = f"{string}{chars[index]}"

        excluded_string: bool = False
        try:
            for exclution in exclutions:
                if string.__contains__(exclution):
                    raise Exception
        except (Exception):
            excluded_string = True

        if not (excluded_string):
            strings.append(string)