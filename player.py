from deck import Deck

class Player(object):
    def __init__(self, name, money=100):
        self.name = name
        self.money = money
        self.hand = []
        self.game = None
        self.bet = 0

    def join_game(self, game):
        # TODO
        pass

    def stand(self):
        # TODO
        pass

    def hit(self):
        # TODO
        pass

    def bet(self, amount):
        self.bet += amount
        self.money -= amount
        print("{} has bet a total of {}. They have {} remaining.".format(self.name, self.bet, self.money))

    def double(self):
        # TODO
        pass

    def own_hand(self):
        for card in self.hand:
            print(card.get_name())

    def show_hand(self):
        for card in self.hand:
            if card.revealed:
                print(card.get_name)
            else:
                print("This card has not been revealed.")

    def look_at_hand(self, player):
        player.show_hand()


class Dealer(Player):
    def __init__(self, game, name="Dealer"):
        Player.__init__(self, name)
        self.game = game
        self.deck = Deck(game.get_deck_type(), )

    def take_turn(self):
        # TODO
        pass

    def deal(self):
        # TODO
        pass

    def start_game(self):
        self.deck.shuffle()
