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

#Write your code below this line 👇
UserChoice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
map=[rock, paper, scissors]
ComputerChoice=random.randint(0, 2)
print(f" The Computer's Choice is : \n{map[ComputerChoice]}")
print(f" The Users's Choice is : \n{map[UserChoice]}")

if ComputerChoice==0 and UserChoice==1:
    print("You Win")
elif ComputerChoice==1 and UserChoice==2:
    print("You Win")
elif ComputerChoice==2 and UserChoice==0:
    print("You Win! ")
elif ComputerChoice==UserChoice:
    print("Its a Draw!")
else:
    print("You Lose")