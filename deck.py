from card import Card


class Deck(object):
    types = {"Standard": [Card("Ace", "Hearts"), Card("Two", "Hearts"), Card("Three", "Hearts"), Card("Four", "Hearts"),
                          Card("Five", "Hearts"), Card("Six", "Hearts"), Card("Seven", "Hearts"),
                          Card("Eight", "Hearts"), Card("Nine", "Hearts"), Card("Ten", "Hearts"),
                          Card("Jack", "Hearts"), Card("Queen", "Hearts"), Card("King", "Hearts"),
                          Card("Ace", "Spades"), Card("Two", "Spades"), Card("Three", "Spades"), Card("Four", "Spades"),
                          Card("Five", "Spades"), Card("Six", "Spades"), Card("Seven", "Spades"),
                          Card("Eight", "Spades"), Card("Nine", "Spades"), Card("Ten", "Spades"),
                          Card("Jack", "Spades"), Card("Queen", "Spades"), Card("King", "Spades"),
                          Card("Ace", "Clubs"), Card("Two", "Clubs"), Card("Three", "Clubs"), Card("Four", "Clubs"),
                          Card("Five", "Clubs"), Card("Six", "Clubs"), Card("Seven", "Clubs"),
                          Card("Eight", "Clubs"), Card("Nine", "Clubs"), Card("Ten", "Clubs"),
                          Card("Jack", "Clubs"), Card("Queen", "Clubs"), Card("King", "Clubs"),
                          Card("Ace", "Diamonds"), Card("Two", "Diamonds"), Card("Three", "Diamonds"),
                          Card("Four", "Diamonds"),
                          Card("Five", "Diamonds"), Card("Six", "Diamonds"), Card("Seven", "Diamonds"),
                          Card("Eight", "Diamonds"), Card("Nine", "Diamonds"), Card("Ten", "Diamonds"),
                          Card("Jack", "Diamonds"), Card("Queen", "Diamonds"), Card("King", "Diamonds")]}

    def __init__(self, deck_type, size=1):
        self.cards = []
        x = 0
        while x in range(size):
            try:
                self.cards.extend(Deck.types[deck_type])
                x += 1
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
        return self.cards.pop()
