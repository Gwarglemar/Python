#imports
from deck import Deck
from player import Player
from dealer import Dealer


def deal_card(person,deck,how_many):
    iter = 1
    while iter <= how_many:
        person.hand.append(deck.deal_card())
        iter += 1


#display game-state
def show_hands(revealed=False):
    print("\n")
    dealer.show_hand(revealed)
    if revealed:
        print("Dealer hand value: " + str(dealer.get_hand_value()))
    print("------------")
    player.show_hand()
    print("Player hand value: " + str(player.get_hand_value()))
    print("\n")


def ask_hit():
    while True:
        x = input("Hit or Stay?: ")
        if x.lower() == "hit":
            return True
        elif x.lower() == "stay":
            return False
        else:
            print("Invalid input.")
            

def hit(person):
    deal_card(person,deck,1)


def check_bust(person):
    if person.get_hand_value() > 21:
        return True
    else:
        return False

def place_bet():
    print("Current chip total: " + str(player.get_chip_total()))
    while True:
        bet = input("Place bet: (integer between 1 and " + str(player.get_chip_total()) + "): ")
        try:
            bet = int(bet)
            if bet < 1 or bet > player.get_chip_total():
                print("Invalid input.")
            else:
                player.remove_chips(bet)
                return bet
        except:
            print("Invalid input.")
        

def check_win():
    if dealer.get_hand_value() == 21 and len(dealer.hand) == 2:
        return False
    elif player.get_hand_value() == 21 and len(player.hand) == 2:
        return True
    elif dealer.get_hand_value() > 21 and player.get_hand_value() <= 21:
        return True
    elif dealer.get_hand_value() < player.get_hand_value():
        return True
    else:
        return False


#run the game
#init our variables
dealer  = Dealer()
player  = Player()
deck    = Deck()

#game loop
while True:
    #place bet
    bet = place_bet()
    
    #deal the initial hands
    deal_card(dealer,deck,2)
    deal_card(player,deck,2)

    show_hands()
    #loop until player busts or stands
    while ask_hit():
        hit(player)
        show_hands()
        if check_bust(player):
            break
    #player stands; if not bust, dealer turn loop
    if check_bust(player):
        print("Player bust!")
        print("Current chip total: " + str(player.get_chip_total()))
        print("\n")
    else:
        #dealer goes until at least 17
        while dealer.get_hand_value() < 17:
            deal_card(dealer,deck,1)
        #show hands, check win/lose
        show_hands(revealed=True)
        if check_win():
            print("Player win!")
            #add twice as many chips, because we took their bet away initially.
            player.add_chips(bet*2)
            print("Current chip total: " + str(player.get_chip_total()))
            print("\n")
        else:
            print("Dealer wins!")
            print("Current chip total: " + str(player.get_chip_total()))
            print("\n")

    #play again?
    #if no chips, can't play again
    if player.get_chip_total() <= 0:
        print("Player is out of money, better hit the bank before playing again.")
        break
    #else, ask if play again
    play_again = ''
    while True:
        play_again = input("Play again? (y or n): ")
        if play_again.lower() == 'y' or play_again == 'n':
            break
        else:
            print("Invalid input.")

    if play_again.lower() == 'n':
        break
    else:
        #reset the game-state
        deck = Deck()
        player.clear_hand()
        dealer.clear_hand()