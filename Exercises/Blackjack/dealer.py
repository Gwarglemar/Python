from person import Person

class Dealer(Person):

    def show_hand(self,revealed=False):
        output = "Dealer's hand: "
        x = 1
        for card in self.hand:
            if x == 1 and revealed == False:
                output = output + '<HIDDEN>' + ' | '
                x += 1
            else:    
                output = output + str(card) + ' | '
        print(output)