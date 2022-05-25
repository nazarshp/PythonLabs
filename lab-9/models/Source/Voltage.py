from models.Source.Source import Source


class Voltage(Source):
    def __init__(self, name: str, serial_number: str, power: int) -> None:
        super().__init__(name, serial_number)
        self.power = power

    def __str__(self) -> str:
        return f'{super().__str__()};  Power: {self.power}(Bt).'