import random
import os


Image = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

Moves = ["rock","paper","scissors"]

Computer_Lose = {
  "rock": "scissors",
  "scissors": "paper",
  "paper": "rock"
}

player = None
game_is_on = True
while game_is_on:
  os.system("cls")
  while Image.get(player) is None:
    player = input("Choose between Rock, Paper, Scissors: ").lower()

  computer = random.choice(list(Image.keys()))


  if player == "rock":
    print("rock-Image")
  elif player == "paper":
    print("paper-Image")
  elif player == "scissors":
    print('scissors-Image')


  print(Image[player])
  print('Computer:', computer)
  print(Image[computer])

  if player == computer:
    print("It's a tie")
  else:
    if Computer_Lose[player] == computer:
      print("You won!!!")
    else:
      print("You lost...")

  game_is_on = input("You want to play again ?").lower() == "yes"
  player = None

