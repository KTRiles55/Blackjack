# Description
A simplified version of the card game, BlackJack, programmed using Python. The user will challenge a computer-generated dealer that will assign you a random hand of 2 cards in each round and will be able to draw a new card by "hitting" or choose to "stand" by not drawing any cards until the dealer's turn. The winner is determined by which player has the higher score and must be at most 21, otherwise it results in a "Bust", which is an automatic loss. The user can play as many times as they want until they or the dealer run out of chips.

# User manual

## Step 1:
Install the source file, blackjack.py, and navigate to the directory where it is located using the OS command shell.

## Step 2: 
Run the command "python blackjack.py" to start the game.

## Step 3:
The user is asked by the program if they want to play the game or not. They can enter either \["Yes", "yes", "Y", "y"] to play or \["No", "no", "N", "n"] to not play.

![Screenshot (107)](https://github.com/user-attachments/assets/71ddfd4b-98ea-4457-8e53-af6d14f4bbe2)

## Step 4:
Once the user agrees to play, they are asked to enter how much they want to bet. The number of chips that the user can bet can only be a positive number that is less than the total number of chips in hand or equal the total number of chips to "go all-in".

![Screenshot (108)](https://github.com/user-attachments/assets/128253b9-8c3a-473e-924c-56cb3d20c926)

## Step 5: 
After placing their bet, the user is dealt two cards and can see their current score, which is the sum value of the cards in their hand. They are asked if they want to "hit" (draw a card) or "stand" (stop drawing cards). 

![Screenshot (109)](https://github.com/user-attachments/assets/3f34fc7a-c277-45d6-9e3c-46206fd1dfef)

## Step 6:
If the user chooses to hit, they can keep on going until they select "stand" or if they reach a "bust".

![Screenshot (110)](https://github.com/user-attachments/assets/e7bbc8db-9cf9-4292-817a-8c543b2551e4)

## Step 7: 
When the user chooses to stand, it is the dealer's turn. After the dealer stands or reaches a bust, the winner is decided by comparing the scores. If one of the scores is higher and not a bust, the player with that score wins. Finally, the program asks the user if they want to play again (same input from Step #1 is applies here).

![Screenshot (112)](https://github.com/user-attachments/assets/20c645ca-5b9b-4b1c-9ed9-11a1a4c46e6c)
