import random
from random import choice

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice >= 0 and player_choice <=2:
    print(options[player_choice])

computer_choice = random.randint(0,2)
print("Computer choose:")
print(options[computer_choice])

if player_choice < 0 or player_choice >=3:
    print("You lose.")
    print("Invalid number. Please enter a valid number from 0 to 2.")
elif player_choice == 0 and computer_choice == 2:
    print("You Win.")
elif player_choice == 1 and computer_choice == 0:
    print("You Win.")
elif player_choice == 2 and computer_choice == 1:
    print("You win.")
elif player_choice == computer_choice:
    print("It's a Draw.")
else:
    print("You lose.")
