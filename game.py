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
        self.players.append(self.dealer)
        self.pot = 0
        self.turn = 0

    def add_to_pot(self, amount):
        self.pot += amount

    def win(self, player):
        # TODO
        pass

    def bust(self, player):
        # TODO
        pass

    def evaluate_hand(self, player, hand):
        value = 0
        for card in hand:
            if card.get_face() == "Ace":
                # TODO: Check rules and see if ace can be high, modify if necessary
                value += 1
            elif card.get_face() == "Two":
                value += 2
            elif card.get_face() == "Three":
                value += 3
            elif card.get_face() == "Four":
                value += 4
            elif card.get_face() == "Five":
                value += 5
            elif card.get_face() == "Six":
                value += 6
            elif card.get_face() == "Seven":
                value += 7
            elif card.get_face() == "Eight":
                value += 8
            elif card.get_face() == "Nine":
                value += 9
            elif card.get_face() in ["Ten", "Jack", "Queen", "King"]:
                value += 10
        if value == 21:
            print("{} has twenty-one!".format(player.name))
            self.win(player)
        elif value > 21:
            print("{} has busted!".format(player.name))
            self.remove_player(player)
        else:
            return value

    def remove_player(self, player):
        print("{} is out of the game!".format(player.name))
        self.players.remove(player)
        if len(self.players) == 1:
            self.win(self.players[0])
        else:
            self.next_turn()

    def game_over(self):
        # TODO
        pass

    def next_turn(self):
        if self.turn in range(len(self.players)):
            self.turn += 1
        else:
            self.turn = 0
        try:
            self.players[self.turn].take_turn()
        except:
            self.dealer.take_turn()

    def get_starting_hand(self):
        return Blackjack.starting_hand
