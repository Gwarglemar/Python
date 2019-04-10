from person import Person

class Player(Person):

    def __init__(self,starting_chips=100):
        self.hand = []
        self.chips = starting_chips
    
    def show_hand(self):
        output = "Player's hand: "
        for card in self.hand:
            output = output + str(card) + ' | '
        print(output)

    def remove_chips(self,qty):
        if self.chips < qty:
            self.chips = 0
        else:
            self.chips = self.chips - qty

    def add_chips(self,qty):
        self.chips += qty

    def get_chip_total(self):
        return self.chips