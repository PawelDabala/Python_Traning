from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str


queen_of_hearts = DataClassCard('Q', 'Hearts')
# print(queen_of_hearts.rank)
# print(queen_of_hearts)
# print(queen_of_hearts == DataClassCard('Q', 'Hearts'))


#Basic Data Casses
@dataclass
class Position:
    name: str
    lon: float
    lat: float

pos = Position('Oslo', 10.8, 59.9)
print(pos)
print(pos.lat)
print(pos.name)