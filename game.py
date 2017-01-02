class Game(object):
    def __init__(self, deck_type):
        self.deck_type = deck_type

    def get_deck_type(self):
        return self.deck_type


class Blackjack(Game):
    def __init__(self):
        # TODO
        Game.__init__(self, "Standard")

    def win(self, player):
        # TODO
        pass

    def game_over(self):
        # TODO
        pass
