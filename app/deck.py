import random
import numpy as np
from app.card import Card


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(52):
            self.cards.append(Card(i+1))

    def deal(self):
        return self.cards.pop()

    def collect(self, card):
        self.cards.append(card)

    def validate(self):
        if len(self.cards) != 52:
            return False
        bool_arr = [0 for i in range(52)]
        for card in self.cards:
            bool_arr[ card.id() - 1 ] = 1
        for index in range(52):
            if bool_arr[index] != 1:
                return False
        return True

    def shuffle(self):
        random.shuffle(self.cards)

    def riffle(self, perfect = None):
        shuffled_deck = []
        left_half = self.cards[0:len(self.cards)//2]
        right_half = self.cards[len(self.cards)//2:]
        if perfect is None:
            while(len(left_half) > 0 and len(right_half) > 0):
                which = bool(random.getrandbits(1))
                if(which):
                    shuffled_deck.append(left_half.pop())
                else:
                    shuffled_deck.append(right_half.pop())
            shuffled_deck += left_half + right_half
        else:
            for i in range(52):
                if(i%2==0):
                    shuffled_deck.append(left_half.pop())
                else:
                    shuffled_deck.append(right_half.pop())
        self.cards = shuffled_deck

    def hindu(self, segments = 6, perfect = None):
        shuffled_deck = []
        if perfect is None:
            rand_split = [random.randint(0, 51) for i in range(segments-1)]
            rand_split.sort()
            shuffled_deck = self.cards[0:rand_split[0]]
            for i in range(segments-2):
                shuffled_deck = self.cards[rand_split[i]:rand_split[i+1]] + shuffled_deck
            shuffled_deck = self.cards[rand_split[-1]:] + shuffled_deck
        else:
            perfect_split = [(52//segments) * (i+1) for i in range(segments-1)]
            shuffled_deck = self.cards[0:perfect_split[0]]
            for i in range(segments-2):
                shuffled_deck = self.cards[perfect_split[i]:perfect_split[i+1]] + shuffled_deck
            shuffled_deck = self.cards[perfect_split[-1]:] + shuffled_deck
        self.cards = shuffled_deck

    def cut(self, perfect = None):
        if perfect is None:
            cut_point = random.randint(0, 51)
            self.cards = self.cards[cut_point:] + self.cards[0:cut_point]
        else:
            self.cards = self.cards[52//2:] + self.cards[0:52//2]

    def __str__(self):
        retstr = ""
        for card in self.cards:
            retstr += "[" + str(card) + "]\n"
        return retstr

    @staticmethod
    def shuffle_score(deck):
        ctr = 0
        streak_bonus = 0
        last = deck.cards[0].id()
        for i in range(1, 52):
            if deck.cards[i].id() == last + 1:
                ctr += 1 + streak_bonus
                streak_bonus += 1
            else:
                streak_bonus = 0
            last = deck.cards[i].id()
        return ctr

    @staticmethod
    def variation_distance(shuffle_func, trials = 100000):
        distribution = np.matrix([[0 for i in range(52)] for i in range(52)])
        for trial in range(trials):
            new_deck = Deck()
            new_deck = shuffle_func(new_deck)
            for j in range(1, 53):
                # Examining card ID: j+1
                final_position = new_deck.cards.index(j)
                distribution[j-1, final_position] += 1
        distribution = distribution / trials
        uniform = np.matrix([[1/52 for i in range(52)] for i in range(52)])
        distance = (distribution - uniform)/2
        sum_distance = np.sum(np.abs(distance), 1)
        normalized = np.sum(sum_distance)/52
        return(normalized)  

