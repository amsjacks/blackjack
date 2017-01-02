from game import Game
from deck import Deck

class Player(object):
    def __init__(self, name, money=100):
        self.name = name
        self.money = money
        self.hand = []

    def stand(self):
        # TODO
        pass

    def hit(self):
        # TODO
        pass

    def bet(self, amount):
        # TODO
        pass


class Dealer(Player):
    def __init__(self, game, name="Dealer"):
        Player.__init__(self, name)
        self.game = game
        self.deck = Deck(game.get_deck_type())

    def take_turn(self):
        # TODO
        pass

    def deal(self):
        # TODO
        pass

    def start_game(self):
        # TODO
        self.deck.shuffle()