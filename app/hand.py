from app.card import Card

class Hand:
    def __init__(self, card1, card2):
        if card1 > card2:
            self.card1 = card1
            self.card2 = card2
        elif card2 > card1:
            self.card1 = card2
            self.card2 = card1
        elif Card.same_suit(card1, card2):
            raise ValueError("Both cards cannot be identical: %s, %s." % (card1, card2))
        else:
            self.card1 = card1
            self.card2 = card2

    def __str__(self):
        retstr = ""
        retstr += self.card1.value_name()
        retstr += self.card2.value_name()
        return retstr