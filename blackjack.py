import random

class card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return "card(rank: {}, suit: {})".format(self.rank, self.suit)

class deck(object):
    rank_list = ['A'] + [str(i) for i in range(2,11)] + list('JQK')
    suit_list = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

    def __init__(self):
        self._cards = [card(rank, suit) for suit in self.suit_list
                                        for rank in self.rank_list]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        return self._cards.pop() if len(self) else None

    def cut(self, position):
        self._cards = self._cards[position:] + self._cards[:position]

class hand(object):
    def __init__(self, deck):
        self.init_hand = [deck.deal(), deck.deal()]

    def hit(self, deck):
        self.init_hand.append(deck.deal())

    def points(self):
        pass
        


my_deck = deck()
my_deck.shuffle()
for i in my_deck._cards:
    print(i)
print(len(my_deck._cards))
my_deck.cut(28)
for i in my_deck._cards:
    print(i)
user_hand = hand(my_deck)
user_hand.hit(my_deck)
print(user_hand.init_hand)
for i in my_deck._cards:
    print(i)
print(len(my_deck._cards))
