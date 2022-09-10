
class Animal:
    def __init__(self, color, number_of_legs) -> None:
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs
    def __str__(self) -> str:
        return f'{self.species} {self.color} {self.number_of_legs}'


class FourLeggedAnimal(Animal):
    def __init__(self, color) -> None:
        super().__init__(color, 4)


class TwoLeggedAnimal(Animal):
    def __init__(self, color) -> None:
        super().__init__(color, 2)


class sheep(FourLeggedAnimal):
    species = 'sheep'
    def __init__(self, color) -> None:
        super().__init__(color)


class Parrot(TwoLeggedAnimal):
    def __init__(self, color) -> None:
        super().__init__(color)

s = sheep("white")
print(s)

parrot = Parrot("grey")
print(parrot)