class Deck(object):
    types = {"Standard": [("Ace", "Hearts"), ("Two", "Hearts"), ("Three", "Hearts"), ("Four", "Hearts"),
                          ("Five", "Hearts"), ("Six", "Hearts"), ("Seven", "Hearts"),
                          ("Eight", "Hearts"), ("Nine", "Hearts"), ("Ten", "Hearts"),
                          ("Jack", "Hearts"), ("Queen", "Hearts"), ("King", "Hearts"),
                          ("Ace", "Spades"), ("Two", "Spades"), ("Three", "Spades"), ("Four", "Spades"),
                          ("Five", "Spades"), ("Six", "Spades"), ("Seven", "Spades"),
                          ("Eight", "Spades"), ("Nine", "Spades"), ("Ten", "Spades"),
                          ("Jack", "Spades"), ("Queen", "Spades"), ("King", "Spades"),
                          ("Ace", "Clubs"), ("Two", "Clubs"), ("Three", "Clubs"), ("Four", "Clubs"),
                          ("Five", "Clubs"), ("Six", "Clubs"), ("Seven", "Clubs"),
                          ("Eight", "Clubs"), ("Nine", "Clubs"), ("Ten", "Clubs"),
                          ("Jack", "Clubs"), ("Queen", "Clubs"), ("King", "Clubs"),
                          ("Ace", "Diamonds"), ("Two", "Diamonds"), ("Three", "Diamonds"), ("Four", "Diamonds"),
                          ("Five", "Diamonds"), ("Six", "Diamonds"), ("Seven", "Diamonds"),
                          ("Eight", "Diamonds"), ("Nine", "Diamonds"), ("Ten", "Diamonds"),
                          ("Jack", "Diamonds"), ("Queen", "Diamonds"), ("King", "Diamonds")]}

    def __init__(self, deck_type, size=1):
        self.cards = []
        x = 0
        while x in range(size):
            try:
                self.cards.extend(Deck.types[deck_type])
            except:
                print("Error: deck type is not supported")
                break

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        # TODO
        pass

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def next_card(self):
        return self.cards.pop(0)
