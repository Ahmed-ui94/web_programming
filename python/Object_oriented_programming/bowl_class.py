from typing import List
from dataclasses import dataclass, field


@dataclass
class Scoop:
    flavour: str

@dataclass
class Bowl():
    scoops: List[Scoop] = field(default_factory=list)
    # class attribute
    bowl_limit = 3
    
    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) < self.bowl_limit:
                self.scoops.append(one_scoop)
    
    def __repr__(self):
        return '\n'.join(s.flavour for s in self.scoops)

# a class that inherites from bowl class but modifies the class variable of bowl
class BigBowl(Bowl):
    bowl_limit = 5

s1 = Scoop("chocolate")
s2 = Scoop("Permison")
s3 = Scoop("Orange")
s4 = Scoop("mango")
b = Bowl()
b.add_scoops(s1, s2, s3, s4)
print(b)
b2 = BigBowl()
b2.add_scoops(s1, s2, s3, s4)
print(b2)