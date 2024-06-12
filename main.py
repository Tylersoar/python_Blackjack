import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.calculate_value()

    def calculate_value(self):
        values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
                  'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
                  'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        return values[self.rank]

    def shuffle(Card_deck):
        random.shuffle(Card_deck)
        return Card_deck

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Dealer():
    def __init__(self, cards=[]):
        self.cards = cards

    def play_blackJack(self):
        self.cards = [shuffled_deck.pop(), shuffled_deck.pop()]

        while sum(card.value for card in self.cards) < 17:
            self.cards.append(shuffled_deck.pop())

        print(f"Dealer's final hand: {[str(card) for card in self.cards]}")
        dealer_hand_value = sum(card.value for card in self.cards)

        return dealer_hand_value


class Player:
    def __init__(self, number_of_chips, cards=[]):
        self.number_of_chips = number_of_chips
        self.cards = cards
        self.bet_amount = 0

    def bet(self):
        bet_amount = int(input(f"you have {self.number_of_chips} chips, enter a amount to bet: "))
        if 0 < bet_amount <= self.number_of_chips:
            self.bet_amount = bet_amount
            self.number_of_chips -= bet_amount
            print(f"you betted {bet_amount} and have {self.number_of_chips} remaining")
        else:
            print("insufficient chips")

    def calculate_hand_value(self):
        return [card.value for card in self.cards]

    def play_blackjack(self):
        again = True
        while again:
            if self.number_of_chips > 0:
                self.bet()
                # Deal two initial cards
                self.cards = [shuffled_deck.pop(), shuffled_deck.pop()]

                while sum(card.value for card in self.cards) < 21:
                    print(f"Your current hand: {[str(card) for card in self.cards]}")
                    action = input("Do you want to 'hit' or 'stand'? ").lower()

                    if action == 'hit':
                        self.cards.append(shuffled_deck.pop())
                    elif action == 'stand':
                        break
                    else:
                        print("Invalid input. Please enter 'hit' or 'stand'.")

                print(f"Your final hand: {[str(card) for card in self.cards]}")
                player_hand_value = sum(card.value for card in self.cards)

                dealer = Dealer()
                dealer_hand_value = dealer.play_blackJack()
                self.determine_winner(player_hand_value, dealer_hand_value)

                if player_hand_value == 21:
                    self.number_of_chips += 2 * self.bet_amount
                elif player_hand_value <= 21 and (dealer_hand_value > 21 or player_hand_value > dealer_hand_value):
                    self.number_of_chips += 2 * self.bet_amount

                choice = input("Want to play again Y/N: ").lower()

                if choice == 'Y':
                    again = True
                elif choice == 'N':
                    break

            else:
                print("Insufficient amount of chips.")

    def determine_winner(self, player_hand_value, dealer_hand_value):

        if player_hand_value == 21:
            print("Congratulations! You got Blackjack")
        elif player_hand_value > 21:
            print("Busted! you went over 21. You lose")
        elif dealer_hand_value == 21:
            print("Dealer got Blackjack! You lose")
        elif dealer_hand_value > 21:
            print("Dealer busted! You win")
        elif player_hand_value > dealer_hand_value:
            print("You win!")
        elif player_hand_value < dealer_hand_value:
            print("You lose.")
        else:
            print("It's a tie")


deck = []
suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
ranks = ['Two', 'Three', 'Four', 'Five', 'Six',
         'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace']

for suit in suits:
    for rank in ranks:
        card = Card(suit, rank)
        deck.append(card)

# Shuffle the deck
shuffled_deck = Card.shuffle(deck)

# Create a player with 100 chips
player1 = Player(100)


player1.play_blackjack()
