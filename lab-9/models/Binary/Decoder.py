from models.Binary.Binary import Binary


class Decoder(Binary):
    def __init__(self, name: str, price: int, key: str) -> None:
        super().__init__(name, price)
        self.key = key

    def __str__(self) -> str:
        return f'{super().__str__()}  Key: {self.key}.'