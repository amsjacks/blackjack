class Game(object):
    def __init__(self, deck_type):
        self.deck_type = deck_type

    def get_deck_type(self):
        return self.deck_type


class Blackjack(Game):
    starting_hand = 2

    def __init__(self, decks=1):
        # TODO
        Game.__init__(self, "Standard")
        self.decks = decks


    def win(self, player):
        # TODO
        pass

    def bust(self, player):
        # TODO
        pass

    def game_over(self):
        # TODO
        pass


