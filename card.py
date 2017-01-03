class Card(object):
    def __init__(self, face, suit, name=None):
        self.suit = suit
        self.face = face
        self.name = name
        self.revealed = False

    def get_name(self):
        if self.name:
            return self.name
        else:
            return "{} of {}".format(self.face, self.suit)

    def reveal(self):
        self.revealed = True