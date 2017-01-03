from deck import Deck


deck = Deck("Standard")
deck.shuffle()
print(deck.next_card().get_name())