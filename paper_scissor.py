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

# list of choices
choice = [rock, paper, scissors]
choice_desc = ["rock", "paper", "scissor"]

# get input from the user
player_choice = int(
    input('''
What do you choose?
-> Enter '0' for 'Rock'
-> Enter '1' for 'Paper'
-> Enter '2' for 'Scissor'

'''))

if player_choice > 2 or player_choice < 0:
    print("Invalid Number, Plesae Enter Again!")
    quit()

print(f"User choice is {choice_desc[player_choice]} : ")
print(choice[player_choice])

# machine choose a random from number 0 and 2
machine_choice = random.randint(0, 2)
print(f"Machine choice is {choice_desc[machine_choice]} : ")
print(choice[machine_choice])

# output player result
if player_choice == machine_choice:
    print("Draw")
elif player_choice == 0 and machine_choice == 2:
    print("You Win!!!")
elif player_choice == 1 and machine_choice == 0:
    print("You Win!!!")
elif player_choice == 2 and machine_choice == 1:
    print("You Win!!!")
else:
    print("You Lose!!!")
