from game import Blackjack

class Player(object):
    def __init__(self, name, money=100):
        self.name = name
        self.money = money
        self.hand = []
        self.game = None
        self.bet = 0

    def join_game(self, game):
        game.add_player(self)
        self.game = game

    def start_game(self, game_type):
        if game_type == "Blackjack":
            self.game = Blackjack([self])
        else:
            print("That game type is not available.")

    def stand(self):
        # TODO
        pass

    def hit(self):
        # TODO
        pass

    def bet(self, amount):
        self.bet += amount
        self.game.add_to_pot(amount)
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






