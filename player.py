from game import Blackjack

class Player(object):
    def __init__(self, name, money=100):
        self.name = name
        self.money = money
        self.hand = []
        self.game = None
        self.bet = 0
        self.has_doubled = False

    def join_game(self, game):
        game.add_player(self)
        self.game = game

    def start_game(self, game_type):
        if game_type == "Blackjack":
            self.game = Blackjack([self])
            return self.game
        else:
            print("That game type is not available.")

    def stand(self):
        self.game.next_turn()

    def hit(self):
        if self.has_doubled:
            print("As you doubled last turn, you must stand.")
            self.stand()
        else:
            dealer = self.game.get_dealer()
            self.add_to_hand(dealer.deal())
            self.show_hand()
            if self.game.win(self) or self.game.bust(self):
                # TODO: finish implementing once I figure out how I want to end games
                pass
            else:
                self.game.next_turn()

    def bet(self, amount):
        self.bet += amount
        self.game.add_to_pot(amount)
        self.money -= amount
        print("{} has bet a total of {}. They have {} remaining.".format(self.name, self.bet, self.money))

    def add_to_money(self, amount):
        self.money += amount

    def double(self):
        # TODO
        pass

    def add_to_hand(self, card):
        self.hand.append(card)

    def own_hand(self):
        for card in self.hand:
            print(card.get_name())

    def show_hand(self):
        for card in self.hand:
            if card.revealed:
                print(card.get_name())
            else:
                print("This card has not been revealed.")

    def take_turn(self):
        # TODO: Think about expanding this into an instance of eventual Menu class
        print("Player takes turn")


    def dealer_hand(self):
        self.game.get_dealer().show_hand()