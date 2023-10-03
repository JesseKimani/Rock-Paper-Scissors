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

#Write your code below this line 👇
import random

choice= input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n")
comp_choice= random.randint(0 , 2)

if choice == "0":
  print(rock)
  print("Computer chose:")
  if comp_choice == 0:
    print(rock + "Draw")
  elif comp_choice == 1:
    print(paper + "You lose")
  elif comp_choice == 1:
    print(scissors + "You win!")

elif choice == "1":
  print(paper)
  print("Computer chose:")
  if comp_choice == 0:
    print(rock + "You win!")
  elif comp_choice == 1:
    print(paper + "Draw")
  elif comp_choice == 1:
    print(scissors + "You lose")

elif choice == "2":
  print(scissors)
  print("Computer chose:")
  if comp_choice == 0:
    print(rock + "You lose")
  elif comp_choice == 1:
    print(paper + "You win")
  elif comp_choice == 1:
    print(scissors + "Draw")

else:
  print("You picked an invalid number. You lose!")