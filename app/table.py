from app.card import Card
from app.hand import Hand
from app.deck import Deck

class Table:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        