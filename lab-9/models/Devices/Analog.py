from models.Devices.Devices import Devices


class Analog(Devices):
    def __init__(self, name: str, price: int, serial_number: str, frequency: int) -> None:
        super().__init__(name, price, serial_number)
        self.frequency = frequency

    def __str__(self) -> str:
        return f'{super().__str__()};  Frequency: {self.frequency}(Hz)'
