from models.Source.Source import Source


class Current(Source):
    def __init__(self, name: str, serial_number: str, resistance: int) -> None:
        super().__init__(name, serial_number)
        self.resistance = resistance

    def __str__(self) -> str:
        return f'{super().__str__()};  Resistance: {self.resistance}(Om).'

