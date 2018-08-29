
class Card:
    def __init__(self, id):
        # id starts with 1 and ends with 52
        value = id % 13
        suit = id // 13
        if value == 0:
            value = 13
            suit -= 1
        if value > 13:
            raise ValueError("Value must be under 13, was %s." % value)
        elif value < 1:
            raise ValueError("Value must be positive, was %s." % value)
        if suit > 3 or suit < 0:
            raise ValueError("Suit must be 0, 1, 2 or 3, was %s." % suit)
        self.value = value
        self.suit = suit

    def __eq__(self, other):
        return self.id() == other 

    def __ne__(self, other):
        return self.value != other.value

    def __gt__(self, other):
        self_value = self.value
        other_value = other.value
        if self_value == 1:
            self_value += 13
        if other_value == 1:
            other_value += 13
        return self_value > other_value

    def __ge__(self, other):
        self_value = self.value
        other_value = other.value
        if self_value == 1:
            self_value += 13
        if other_value == 1:
            other_value += 13
        return self_value >= other_value

    def __lt__(self, other):
        self_value = self.value
        other_value = other.value
        if self_value == 1:
            self_value += 13
        if other_value == 1:
            other_value += 13
        return self_value < other_value

    def __le__(self, other):
        self_value = self.value
        other_value = other.value
        if self_value == 1:
            self_value += 13
        if other_value == 1:
            other_value += 13
        return self_value <= other_value

    def __str__(self):
        retstr = ""
        if self.value == 1:
            retstr += "Ace"
        elif self.value == 11:
            retstr += "Jack"
        elif self.value == 12:
            retstr += "Queen"
        elif self.value == 13:
            retstr += "King"
        else:
            retstr += str(self.value)
        retstr += " of "
        if(self.suit == 0):
            retstr += "Spades"
        elif self.suit == 1:
            retstr += "Hearts"
        elif self.suit == 2:
            retstr += "Clubs"
        elif self.suit == 3:
            retstr += "Diamonds"
        return retstr

    def value_name(self):
        if self.value == 1:
            return "A"
        elif self.value == 13:
            return "K"
        elif self.value == 12:
            return "Q"
        elif self.value == 11:
            return "J"
        elif self.value == 10:
            return "T"
        else:
            return str(self.value)

    def suit_name(self):
        if self.suit == 0:
            return "Spades"
        elif self.suit == 1:
            return "Hearts"
        elif self.suit == 2:
            return "Clubs"
        elif self.suit == 3:
            return "Diamonds"

    def id(self):
        value = self.value
        suit = self.suit
        if(value == 13):
            value = 0
            suit += 1
        return suit * 13 + value

    @staticmethod
    def same_suit(card1, card2):
        return card1.suit == card2.suit