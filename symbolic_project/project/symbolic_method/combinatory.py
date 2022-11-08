class Combinatory:

    def __init__(self, base: int, amount: str, length: int = 0, exclutions: list = []) -> None:  # type: ignore
        self.__base = base
        self.__amount = amount.lower()
        self.__length = length
        self.__exclutions = exclutions

    def get_base(self) -> int:
        return self.__base

    def get_length(self) -> int:
        return self.__length

    def get_amount(self) -> str:
        return self.__amount

    def get_exclutions(self) -> list:
        return self.__exclutions
