rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
import random

rock_ = 0
paper_ = 1
scissors_ = 2

player_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.: ")
)
if player_choice < 0 or player_choice >= 3:
    print("Invalid choice, you lose!")
else:
    if player_choice == 0:
        print(rock)
    if player_choice == 1:
        print(paper)
    if player_choice == 2:
        print(scissors)

    bot_choice = random.randint(0, 2)
    print("Computer chose:")
    if bot_choice == 0:
        print(rock)
    if bot_choice == 1:
        print(paper)
    if bot_choice == 2:
        print(scissors)
    # rock beats scissors; scissors beats paper; paper beats rock
    if player_choice == bot_choice:
        print("It's a draw")
    elif player_choice == 0 and bot_choice == 2:
        print("You win!")
    elif player_choice == 2 and bot_choice == 1:
        print("You win!")
    elif player_choice == 1 and bot_choice == 0:
        print("You win!")
    else:
        print("You lose")
