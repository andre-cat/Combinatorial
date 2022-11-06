from tkinter import messagebox as Messagebox
from symbolic_project.project.symbolic_method.combinatory_class import CombinatoryClass
from symbolic_project.project.symbolic_method import generator


def part_1(option: int, n: int = None) -> list:
    if option == 1:
        return __binary_n_without_00_01(n)
    elif option == 2:
        return __binary_n_without_00_11(n)
    elif option == 3:
        return __ternary_n_without_00(n)
    elif option == 4:
        return __cuaternary_n_crecent_chars()
    elif option == 5:
        return __ternary_n_without_22(n)
    elif option == 6:
        return __ternary_without_22()


def __binary_n_without_00_01(n: int) -> list:
    fn: int
    if n == 0:
        fn = 1
    else:
        fn = 2

    combinatory_class: CombinatoryClass = CombinatoryClass(base=2, length=n, exclutions=['00', '01'], amount=fn)

    return generator.generate(combinatory_class.get_base(), combinatory_class.get_length(), combinatory_class.get_exclutions(), combinatory_class.get_amount())


def __binary_n_without_00_11(n: int) -> list:
    fn: int = None

    combinatory_class: CombinatoryClass = CombinatoryClass(base=2, length=n, exclutions=['00', '11'], amount=fn)

    return generator.generate(combinatory_class.get_base(), combinatory_class.get_length(), combinatory_class.get_exclutions(), combinatory_class.get_amount())


def __ternary_n_without_00(n: int) -> list:
    fn: int = None

    combinatory_class: CombinatoryClass = CombinatoryClass(base=3, length=n, exclutions=['00'], amount=fn)

    return generator.generate(combinatory_class.get_base(), combinatory_class.get_length(), combinatory_class.get_exclutions(), combinatory_class.get_amount())


def __cuaternary_n_crecent_chars(n: int) -> list:
    fn: int = None

    combinatory_class: CombinatoryClass = CombinatoryClass(base=4, exclutions=['crecent'], length=n, amount=fn)

    return generator.generate(combinatory_class.get_base(), combinatory_class.get_length(), combinatory_class.get_exclutions(), combinatory_class.get_amount())


def __ternary_n_without_22(n: int) -> list:
    fn: int = None

    combinatory_class: CombinatoryClass = CombinatoryClass(base=3, length=n, exclutions=['22'], amount=fn)

    return generator.generate(combinatory_class.get_base(), combinatory_class.get_length(), combinatory_class.get_exclutions(), combinatory_class.get_amount())


def __ternary_without_22() -> list:
    fn: int = None

    combinatory_class: CombinatoryClass = CombinatoryClass(base=3, exclutions=['22'], amount=fn)

    return generator.generate(combinatory_class.get_base(), combinatory_class.get_length(), combinatory_class.get_exclutions(), combinatory_class.get_amount())
