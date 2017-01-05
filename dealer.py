from deck import Deck


class Dealer(object):
    def __init__(self, deck_type, game):
        self.deck = Deck(deck_type)
        self.game = game

    def take_turn(self):
        # TODO
        pass

    def deal(self):
        # TODO
        pass

    def first_deal(self):
        self.deck.shuffle()

