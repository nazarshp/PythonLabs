from models.Devices.Devices import Devices


class Pulse(Devices):
    def __init__(self, name: str, price: int, serial_number: str, time_impulse: float) -> None:
        super().__init__(name, price, serial_number)
        self.time_impulse = time_impulse

    def __str__(self) -> str:
        return f'{super().__str__()};   Time Impulse: {self.time_impulse}(s).'