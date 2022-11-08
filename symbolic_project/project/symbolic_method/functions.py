from symbolic_project.project.symbolic_method.combinatory import Combinatory  # type: ignore

def get_function(combinatory: Combinatory):

    file_functions = globals().copy()
    file_functions.update(locals())
    function_name = f'__{combinatory.get_base()}_{combinatory.get_amount()}_e_{chr(95).join(combinatory.get_exclutions())}'
    function = file_functions.get(function_name)
    if not function:
        return None

def __2_n_e_00_01(n: int) -> int:
    fn: int
    if n == 0:
        fn = 1
    else:
        fn = 2

    return fn


def __2_n_e_00_11(n: int) -> list:
    return []


def __3_n_e_00(n: int) -> list:
    return []


def __3_n_e_c(n: int) -> list:
    return []


def __3_n_e_22(n: int) -> list:
    return []


def __3_x_e_22() -> list:
    return []


def __2_n_e_000() -> list:
    return []


def __2_n_e_000_010() -> list:
    return []


def __3_n_e_000() -> list:
    return []
