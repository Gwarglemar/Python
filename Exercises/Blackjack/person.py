class Person():

    def __init__(self):
        self.hand = []


    def clear_hand(self):
        self.hand = []

    def show_hand(self):
        raise NotImplementedError


    def get_hand_value(self):
        value = 0
        aces = 0
        for card in self.hand:
            if card.num == 'A':
                aces += 1
                value += 11
            elif card.num == 'J' or card.num == 'Q' or card.num == 'K':
                value += 10
            else:
                value += int(card.num)
        while aces > 0:
            if value > 21:
                value -= 10
            aces -= 1
        return value