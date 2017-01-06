from deck import Deck

class Dealer(object):
    name = "The dealer"

    def __init__(self, deck_type, game):
        self.deck = Deck(deck_type)
        self.game = game
        self.hand = []

    def take_turn(self):
        score = self.game.evaluate(self.hand)
        if score > 15:
            self.game.next_turn()
        else:
            self.hand.append(self.deal())
            self.game.evaluate(self.hand)
            self.game.next_turn()

    def deal(self):
        card = self.deck.next_card()
        card.reveal()
        return card

    def first_deal(self):
        self.deck.shuffle()
        self.hand.append(self.deck.next_card())
        starting_hand = self.game.get_starting_hand()
        x = 0
        while x in range(starting_hand-1):
            self.hand.append(self.deal())
            x += 1
        y = 0
        while y in range(starting_hand):
            for player in self.game.get_players():
                player.add_to_hand(self.deal())
                y += 1
        print("All hands have been dealt!")
        self.game.next_turn()

    def show_hand(self):
        for card in self.hand:
            if card.revealed:
                print(card.get_name())
            else:
                print("This card has not been revealed.")
