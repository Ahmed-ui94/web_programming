from typing import List, ClassVar, Tuple
from dataclasses import dataclass
import namedtuple
import random


# this demonstates how create class variable using dataclass module
@dataclass(init=False)
class Deck:
    suits: ClassVar[Tuple[str, ...]] = (
        '\N{Black Club Suit}', '\N{White Diamond Suit}',
'\N{White Heart Suit}', '\N{Black Spade Suit}'
    )

    def __init__(self, ) -> None:
        self.cards = [namedtuple.CardPoints(rank=r, suit=s) 
        for r in range(1, 14) 
        for s in self.suits]

        random.shuffle(self.cards)