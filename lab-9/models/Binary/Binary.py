from abc import ABC


class Binary(ABC):
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'Name: {self.name};  Price = {self.price}(usd);'
