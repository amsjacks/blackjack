from player import Player
from game import Game
from game import Blackjack
from deck import Deck
from dealer import Dealer


jack = Player("Jack")
game = jack.start_game("Blackjack")
dealer = game.get_dealer()
dealer.first_deal()
jack.show_hand()
dealer.show_hand()