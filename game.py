from dealer import Dealer

class Game(object):
    def __init__(self, deck_type):
        self.deck_type = deck_type
        self.players = []
        self.dealer = None

    def get_deck_type(self):
        return self.deck_type

    def add_player(self, player):
        self.players.append(player)

    def get_players(self):
        return self.players

    def get_dealer(self):
        return self.dealer


class Blackjack(Game):
    starting_hand = 2
    deck_type = "Standard"
    target_value = 21

    def __init__(self, players, decks=1):
        # TODO: finish
        Game.__init__(self, Blackjack.deck_type)
        self.decks = decks
        assert isinstance(players, list)
        self.players = players
        self.dealer = Dealer(Blackjack.deck_type, self)
        self.pot = 0

    def add_to_pot(self, amount):
        self.pot += amount

    def win(self, player):
        # TODO
        pass

    def bust(self, player):
        # TODO
        pass

    def game_over(self):
        # TODO
        pass

    def get_starting_hand(self):
        return Blackjack.starting_hand
