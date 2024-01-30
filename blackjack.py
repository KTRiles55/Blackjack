# Blackjack Card Game

import random

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card_Type:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        print('{} of {}'.format(self.rank, self.suit))


class Deck_of_cards:

    def __init__(self):

        self.card_stack = []

        for suit in suits:
            for rank in ranks:
                self.card_stack.append(Card_Type(suit, rank))

    def shuffle_cards(self):
        random.shuffle(self.card_stack)

    def deal(self):
        return self.card_stack.pop()


my_stack = Deck_of_cards()


class Hand:

    def __init__(self):

        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self):

        for i in range(2):
            self.cards.append(my_stack.deal())
            self.cards[i] = my_stack.deal()
            self.value += self.cards[i].value

            if self.cards[i].value == 11:
                self.aces = 11

    def adjust_for_aces(self):

        total = self.aces + self.value

        if total > 21 and self.aces == 11:
            print("Adjusting for aces!")
            self.aces = 1
            self.value = self.aces

    def hit(self):

        confirm = False

        while not confirm:

            player_response = input("Will you 'Hit' or 'Stand'? ")
            if player_response == "Hit" or player_response == "hit":

                for i in range(1):
                    self.cards.append(my_stack.deal())
                    self.cards[i] = my_stack.deal()
                    self.value += self.cards[i].value

                    if self.cards[i].value == 11:
                        self.aces = 11

                if self.value >= 21:
                    confirm = True

                print(self.value)

            elif player_response == "Stand" or player_response == "stand":

                confirm = True

                print(self.value)

            else:

                print("Try again.")

    def dealer_hit(self):

        for j in range((self.value >= 16), (self.value < 21)):

            for i in range(1):
                self.cards.append(my_stack.deal())
                self.cards[i] = my_stack.deal()
                self.value += self.cards[i].value

                if self.cards[i].value == 11:
                    self.aces = 11


my_hand = Hand()


class Player:

    def __init__(self):
        self.player_cards = []
        self.player_value = 0

        self.dealer_cards = []
        self.dealer_value = 0

    def deal_player(self):
        self.player_cards.extend(my_hand.cards)
        self.player_value = my_hand.value

    def deal_dealer(self):
        self.dealer_cards.extend(my_hand.cards)
        self.dealer_value = my_hand.value


player = Player()


class Chips:

    def __init__(self):

        self.my_total_chips = 100 + chips_claimed

        self.bet_amount = 0

        self.dealer_chips = 100 + chips_claimed

        self.sum_bets = 0

    def take_bet(self):

        bet = True

        while bet:

            print(self.my_total_chips)
            my_bet = input('How many chips would you like to bet? ')

            bet_made = int(my_bet)

            if type(bet_made) == int:
                if bet_made > self.my_total_chips:
                    print("You don\'t have enough chips for that bet!")
                else:
                    self.my_total_chips = self.my_total_chips - bet_made
                    bet = False
                    print(self.my_total_chips)
                    print('You just bet {} chips'.format(bet_made))


            else:
                print('That is not an amount. Try again!')

            if not bet:

                self.bet_amount = bet_made * 2

                if not self.dealer_chips < bet_made:

                    self.dealer_chips = self.dealer_chips - bet_made

                else:

                    self.dealer_chips = 0
                    print('The dealer is going all in!')

    def win_or_lose_bet(self):

        if player.player_value > 21:

            print("Bust!")

            self.dealer_chips = self.dealer_chips + self.bet_amount
            print(f"The total chips you lost: {self.bet_amount}")

            return self.my_total_chips

        elif (player.player_value < 21) and (player.player_value < player.dealer_value) and (player.dealer_value <= 21):

            self.dealer_chips = self.dealer_chips + self.bet_amount
            print("You lose!")
            print(f"The total chips you lost: {self.bet_amount}")
            chips_claimed = self.bet_amount

            return self.my_total_chips


        elif (player.player_value == player.dealer_value):

            self.my_total_chips = self.my_total_chips + (self.bet_made)
            self.dealer_chips = self.dealer_chips + (self.bet_made)
            print("Push!")
            print(f"Both the player and the dealer reclaim {self.bet_made} chips")
            chips_claimed = self.bet_made

        else:

            self.my_total_chips = self.my_total_chips + self.bet_amount
            print("You win!")
            print(f"The total chips you won: {self.bet_amount}")
            chips_claimed = self.bet_amount

            return self.my_total_chips


game = True
action = input("Do you want to play Blackjack? ")

while (game):

    if (action == "Yes" or action == "yes" or action == "Y" or action == "y"):

        my_stack.shuffle_cards()

        my_stack.deal()

        final_bet = Chips()

        final_bet.take_bet()

        my_hand.add_card()

        player.deal_player()

        my_hand.adjust_for_aces()

        player.deal_player()

        print(player.player_value)

        my_hand.hit()

        player.deal_player()

        my_hand.adjust_for_aces()

        player.deal_player()

        my_hand.value = 0

        my_hand.add_card()

        player.deal_dealer()

        my_hand.adjust_for_aces()

        player.deal_dealer()

        print(player.dealer_value)

        my_hand.dealer_hit()

        player.deal_dealer()

        my_hand.adjust_for_aces()

        player.deal_dealer()

        print(player.player_value)

        print(player.dealer_value)

        final_bet.win_or_lose_bet()

        action = input("Do you want to play again? ")

        my_hand.value = 0

    elif action == "No" or action == "no" or action == "N" or action == "n":

        print("See you next time!")
        game = False

    else:

        print("Please try again.")
        game = False
