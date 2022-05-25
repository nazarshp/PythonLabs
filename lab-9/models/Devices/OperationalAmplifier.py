from models.Devices.Analog import Analog


class OperationalAmplifier(Analog):
    def __init__(self, name: str, price: int, serial_number: str, frequency: int, voltage: int) -> None:
        super().__init__(name, price, serial_number, frequency)
        self.voltage = voltage

    def __str__(self) -> str:
        return f'{super().__str__()};   Voltage: {self.voltage}(B).'
