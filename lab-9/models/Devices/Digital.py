from models.Devices.Devices import Devices


class Digital(Devices):
    def __init__(self, name: str, price: int, serial_number: str, pixel: int) -> None:
        super().__init__(name, price, serial_number)
        self.pixel = pixel

    def __str__(self) -> str:
        return f'{super().__str__()};  Pixel: {self.pixel}.'
