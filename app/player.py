class Player:
    def __init__(self, _id, position, name = "Player", stack):
        self.name = name
        self.hand = None
        self.position = position
        self.stack = stack
        self.id = _id

    def set_name(self, name):
        self.name = name

    def set_hand(self, card1, card2):
        self.hand = Hand(card1, card2)

    def set_position(self, position):
        self.position = position

    def set_stack(self, stack):
        self.stack = stack;

    def set_id(self, _id):
        self.id = _id

    