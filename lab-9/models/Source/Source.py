from abc import ABC


class Source(ABC):
    def __init__(self, name: str, serial_number: str) -> None:
        self.name = name
        self.serial_number = serial_number

    def __str__(self) -> str:
        return f"Name: {self.name}; Serial number: {self.serial_number}"


