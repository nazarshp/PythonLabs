from models.Binary.Binary import Binary


class Adder(Binary):
    def __init__(self, name: str, price: int, discharge: int) -> None:
        super().__init__(name, price)
        self.discharge = discharge

    def __str__(self) -> str:
        return f'{super().__str__()}  Discharge: {self.discharge}(Kl).'