import random

choices = ["rock", "paper", "scissors"]

player_choice = random.choice(choices)
computer_choice = random.choice(choices)

print("Player chose:", player_choice)
print("Computer chose:", computer_choice)

if player_choice == computer_choice:
    print("Draw")
elif player_choice == "rock" and computer_choice == "scissors":
    print("You win")
elif player_choice == "scissors" and computer_choice == "paper":
    print("You win")
elif player_choice == "paper" and computer_choice == "rock":
    print("You win")
else:
    print("You lose")