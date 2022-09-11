
class Animal:
    number_of_legs = 4
    def __init__(self, color) -> None:
        self.species = self.__class__.__name__
        self.color = color
        
    def __repr__(self) -> str:
        return f'{self.species} {self.color} {self.number_of_legs} legs'


class FourLeggedAnimal(Animal):
   Animal.__init__

class TwoLeggedAnimal(Animal):
    number_of_legs = 2
    Animal.__init__


class ZeroLeggedAnimal(Animal):
    number_of_legs = 0
    Animal.__init__


class sheep(FourLeggedAnimal):
    species = 'sheep'
    def __init__(self, color) -> None:
        super().__init__(color)


class Parrot(TwoLeggedAnimal):
    def __init__(self, color) -> None:
        super().__init__(color)

class Snake(ZeroLeggedAnimal):
    def __init__(self, color) -> None:
        super().__init__(color)
    ZeroLeggedAnimal.__repr__
class Wolf(FourLeggedAnimal):
    def __init__(self, color) -> None:
        super().__init__(color)


class Cage:
    def __init__(self, Id) -> None:
        self.cage_list = []
        self.Id = Id


    def add_animals(self, *animals):
        for animal in animals:
            self.cage_list.append(animal)

        return self.cage_list

    def __repr__(self) -> str:
        output = " ".join(anime.species for anime in self.cage_list)
        return f"{self.Id}: {output}"



s = sheep("white")
s2 = sheep("brown")


parrot = Parrot("grey")
p1 = Parrot("white")


snake = Snake("black")
snake2 = Snake("greylish")


wolf = Wolf("maroon")

c1 = Cage(1)
c1.add_animals(s, parrot, snake)
print(c1)

c2 = Cage(2)
c2.add_animals(snake2, p1, s2)
print(c2)