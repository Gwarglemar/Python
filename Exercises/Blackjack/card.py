class Card():

    def __init__(self,suit,num):
        self.suit = suit
        self.num = num

    def __str__(self):
        return str(self.num + ' of ' + self.suit)

    __repr__ = __str__
