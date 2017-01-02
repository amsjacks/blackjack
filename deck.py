class Deck(object):
    types = {"Standard": []} # TODO: Flesh this out once I figure out how I want to represent cards

    def __init__(self, deck_type, size=1):
        self.cards = []
        x = 0
        while x in range(size):
            try:
                self.cards.extend(Deck.types[deck_type])
            except:
                print("Error: deck type is not supported")

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        # TODO
        pass

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)