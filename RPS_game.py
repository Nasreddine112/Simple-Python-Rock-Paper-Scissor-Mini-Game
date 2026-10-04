#                                                         My First Program...
#  A sipmle but cool first-time game made WITHOUT using AI... But only god knows what awaits me in my future programming career... 
#                                        all i know is that it wont be all sunshine and rainbows...

import random

print("Welcome to Rock, Paper, Scissors! Type exit to quit the game.")

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Enter rock, paper, or scissors: ").lower()

    if computer == player:
        print ("Computer chose:", computer)
        print ("Player chose:", player)
        print ("It's a tie!")

    elif player == "rock":
        if computer == "paper":
            print ("Computer chose:", computer)
            print ("Player chose:", player)
            print ("Paper covers rock! You lose!")
        elif computer == "scissors":
            print ("Computer chose:", computer)
            print ("Player chose:", player)
            print ("Rock smashes scissors! You win!")

    elif player == "scissors":
        if computer == "rock":
            print ("Computer chose:", computer)
            print ("Player chose:", player)
            print ("Rock smashes scissors! You lose!")
        elif computer == "paper":
            print ("Computer chose:", computer)
            print ("Player chose:", player)
            print ("Scissors cuts paper! You win!")

    elif player == "paper":
        if computer == "scissors":
            print ("Computer chose:", computer)
            print ("Player chose:", player)
            print ("Scissors cuts paper! You lose!")
        elif computer == "rock":
            print ("Computer chose:", computer)
            print ("Player chose:", player)
            print ("Paper covers rock! You win!")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again == "yes":
        continue
    elif play_again == "no":
        break
    elif play_again != "yes" and play_again != "no":
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue

print("Thanks for playing!")

#                                                            End of program...