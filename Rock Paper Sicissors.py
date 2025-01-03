import random

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

a_list = [rock, paper, scissors]
computer = random.choice(a_list)

ask_for_number = int(input("what do you choose? Type [0] for Rock, [1] for Paper or [2] for Scissors\n"))

if ask_for_number == 0:
    print("You Chose:", a_list[0])
    print("computer chose", computer)
    if computer == a_list[0]:
        print("DRAW!")
    elif computer == a_list[1]:
        print("YOU LOSE!")
    else:
        print("WOU WIN")
else:
    print("That was the wrong Input! Try Again!")
if ask_for_number == 1:
    print("You Chose:", a_list[1])
    print("computer chose", computer)
    if computer == a_list[0]:
        print("YOU WIN!")
    elif computer == a_list[1]:
        print("DRAW!")
    else:
        print("YOU LOSE!")
if ask_for_number == 2:
    print("You Chose:", a_list[2])
    print("computer chose", computer)
    if computer == a_list[0]:
        print("YOU LOSE!")
    elif computer == a_list[1]:
        print("YOU WIN!")
    else:
        print("DRAW")
