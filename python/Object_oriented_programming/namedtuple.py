from typing import NamedTuple, List
from dataclasses import dataclass


# if class is stateless(immutable) use NamedTuple from typing module 
# to create its attributes 
class CardPoints(NamedTuple):
    rank: int
    suit: str

    def points(self) -> int:
        if 1 <= self.rank < 10:
            return self.rank

        return 10

# if class is stateful(mutable) use @dataclass to create its attributes
@dataclass
class CribbageHand():
    cards: List[CardPoints]

    def to_crib(self, card1, card2):
        self.cards.remove(card1)
        self.cards.remove(card2)

cards = [
CardPoints(rank=3, suit='◊ '),
CardPoints(rank=6, suit='♠ '),
CardPoints(rank=7, suit='◊ '),
CardPoints(rank=1, suit='♠ '),
CardPoints(rank=6, suit='◊ '),
CardPoints(rank=10, suit='♡ ')]

ch1 = CribbageHand(cards)
print(ch1)
[c.rank for c in ch1.cards]