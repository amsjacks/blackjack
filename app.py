from player import Player
from game import Game
from game import Blackjack
from deck import Deck
from deck import Card
from dealer import Dealer


jack = Player("Jack")
game = jack.start_game("Blackjack")
dealer = game.get_dealer()
jack = Player("Jack")
game = jack.start_game("Blackjack")
dealer = game.get_dealer()
dealer.first_deal()
jack.show_hand()
jack.dealer_hand()
print(game.evaluate_hand(jack, jack.hand))
print(game.evaluate_hand(dealer, dealer.hand))
game.next_turn()
game.next_turn()
'''
jack = Player("Jack")
game = jack.start_game("Blackjack")
dealer = game.get_dealer()
dealer.add_to_hand(Card("Six", "Hearts"))
dealer.add_to_hand(Card("Two", "Clubs"))
print(game.evaluate_hand(dealer, dealer.hand))
'''
