class Hello:
    """ A Hello class """

    def __init__(self, name: str) -> None:
        self.name = name

    def say_hello(self) -> str:
        return f'Hello {self.name}'
