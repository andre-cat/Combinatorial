import unittest

class generator_test(unittest.TestCase):

    def test_generate(base: int, length: int, exclutions: list):
        strings: list = []
        chars = [None] * length
        generator_test.test__generate(strings, base, length, exclutions, chars, 0)
        return strings;

    def test__generate_(strings : list, base: int, length: int, exclutions: list, chars: list, index: int):

        if index < len(chars):
            for char in range(0, base):
                chars[index] = char
                generator_test.test__generate(strings, base, length, exclutions, chars, index + 1)
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

    base = 2
    length = 9
    exclutions = ['00','01']

    # Print all binary strings
    strings : list = test_generate(base, length, exclutions)
    for string in strings:
        print(string)

if __name__ == '__main__':
    unittest.main()