from abc import ABC


class Devices(ABC):#device
    def __init__(self, name: str, price: int, serial_number: str) -> None:
        self.name = name
        self.price = price
        self.serial_number = serial_number

    def __str__(self) -> str:
        return f'Name: {self.name};  Price = {self.price}(usd);   Serial number: {self.serial_number}'
