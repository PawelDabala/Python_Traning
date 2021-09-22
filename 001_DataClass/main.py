from dataclasses import dataclass, make_dataclass, field
import dataclasses
from typing import List

# @dataclass
# class DataClassCard:
#     rank: str
#     suit: str


# queen_of_hearts = DataClassCard('Q', 'Hearts')
# print(queen_of_hearts.rank)
# print(queen_of_hearts)
# print(queen_of_hearts == DataClassCard('Q', 'Hearts'))


#Basic Data Casses
# @dataclass
# class Position:
#     name: str
#     lon: float
#     lat: float

# pos = Position('Oslo', 10.8, 59.9)
# print(pos)
# print(pos.lat)
# print(pos.name)

# from dataclasses import make_dataclass

# Position = make_dataclass('Position', ['name', 'lat', 'lon'])

#########################################################
# @dataclass
# class Position:
#     name: str
#     lon: float = 0.0 
#     lat: float = 0.0

# print(Position('Null Island'))
# print(Position('Greenwich', lat=51.8))

# from typing import Any

# @dataclass
# class WihoutExpicityTypes:
#     name: Any
#     value: Any = 42

# from dataclasses import dataclass
# from math import asin, cos, radians, sin, sqrt

# @dataclass
# class Position:
#     name: str
#     lon: float = 0.0
#     lat: float = 0.0

#     def distance_to(self, other):
#         r = 6371  # Earth radius in kilometers
#         lam_1, lam_2 = radians(self.lon), radians(other.lon)
#         phi_1, phi_2 = radians(self.lat), radians(other.lat)
#         h = (sin((phi_2 - phi_1) / 2)**2
#              + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
#         return 2 * r * asin(sqrt(h))


# @dataclass
# class PlayingCard:
#     rank: str
#     suit: str


# @dataclass
# class Deck:
#     cards: List[PlayingCard]

# queen_of_hearts = PlayingCard('Q', 'Hearts')
# ace_of_spades = PlayingCard('A', 'Spades')
# two_cards = Deck([queen_of_hearts, ace_of_spades])

# print(two_cards)

# RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
# SUITS = '♣ ♢ ♡ ♠'.split()

# def make_french_deck():
#     return [PlayingCard(r, s) for s in SUITS for r in RANKS]

# @dataclass
# class Deck:
#     cards: List[PlayingCard]= field(default_factory=make_french_deck)

# from dataclasses import fields
# @dataclass
# class Position:
#     name: str
#     lon: float = field(default=0.0, metadata={'unit': 'degrees'})
#     lat: float = field(default=0.0, metadata={'unit': 'degrees'})

# # print(fields(Position))
# lat_unit = fields(Position)[2].metadata['unit']
# print(lat_unit)
# lat = Position('test')
# print(fields(lat))

# next
# You Need Representation?

#########################################################
# @dataclass
# class PlayingCard:
#     rank: str
#     suit: str

#     def __str__(self):
#         return f'{self.suit}{self.rank}'

# ace_of_spades = PlayingCard('A', '♠')
# print(ace_of_spades)

#########################################################
@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

pos = Position('Oslo', 10.8, 59.9)
print(pos.name)
pos.name = 'Stockholm'