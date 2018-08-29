from app.hand import Hand
from app.card import Card
from app.deck import Deck
import datetime

def main():
    test_deck()
    #test_shuffle_strength()
    #shuffle_comparison()
    #test_shuffles()

def shuffle_comparison():
    start_time = datetime.datetime.now()
    print("Trivial:")
    print(Deck.variation_distance(shuffler_trivial))
    print("Single:")
    print(Deck.variation_distance(shuffler_riffle))
    print("Double:")
    print(Deck.variation_distance(shuffler_double_riffle))

    for i in range(3, 9):
        print("%d:" % i)
        print(Deck.variation_distance(lambda deck: shuffler_n_riffle(deck, n=i)))

    print("Python.shuffle:")
    print(Deck.variation_distance(shuffler_shuffle))
        
    print("Casino:")
    print(Deck.variation_distance(shuffler_casino))
    end_time = datetime.datetime.now()
    diff_time = end_time - start_time
    print("Time it took: %d" % diff_time.seconds)

def shuffler_trivial(deck):
    return deck

def shuffler_cut(deck):
    deck.cut()
    return deck

def shuffler_riffle(deck):
    deck.riffle()
    return deck

def shuffler_double_riffle(deck):
    deck.riffle()
    deck.riffle()
    return deck

def shuffler_n_riffle(deck, n=2):
    for i in range(n):
        deck.riffle()
    return deck

def shuffler_7(deck):
    return shuffler_n_riffle(deck, n=7)

def shuffler_casino(deck):
    deck.riffle()
    deck.riffle()
    deck.hindu()
    deck.riffle()
    deck.cut()
    return deck

def shuffler_shuffle(deck):
    deck.shuffle()
    return deck

def test_constructors():
    a = Card(1)
    print(a)

    b = Card(5)
    print(b)

    c = a > b
    print(c)

    print(a.value_name());

    As = Card(4)
    Th = Card(52)
    print( Th) 
    AT = Hand(As, Th)

    print(AT)

def test_shuffles():
    Bicycle = Deck()
    Casino = Deck()

    Casino.cut()
    print("Hindu shuffle:")
    print(Casino)

def test_perfect_riffles():
    for j in range(53):
        x = j
        Montevideo = Deck()
        for i in range(x):
            Montevideo.riffle(perfect = True)

        print("%s perfect riffles:" % x)
        print(Deck.shuffle_score(Montevideo))
        print("\n")


def test_cards():
    Bicycles = Deck()
    for card in Bicycles.cards:
        print(card.id())

def test_shuffle_strength():
    ctr = 0
    for i in range(30000):
        test_deck = Deck()
        test_deck.riffle()
        test_deck.riffle()
        ctr += Deck.shuffle_score(test_deck)
    ctr /= float(30000)
    print(ctr)

def test_deck() :
    Bicycles = Deck()
    assert( Bicycles.validate() )
    some_card = Bicycles.deal()
    assert( not Bicycles.validate() )
    Bicycles.collect(some_card)
    assert( Bicycles.validate() )
    Bicycles.collect(some_card)
    assert( not Bicycles.validate() )

    print( "Test deck passed!")

if __name__ == "__main__":
    main()