import json
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity

card = Card.where(q ='name:Oddish number:122')
#pretty_card = json.dumps(card.__dict__, indent=4)
print(card)
print(card[0]['cardMarket'])