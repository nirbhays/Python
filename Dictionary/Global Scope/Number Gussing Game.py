from random import randint
import art
print(art.logo)
number = randint(1, 100)
#guessed_number=0
runloop = True
#lifes=0
difficulty_level=input("Choose a difficulty. Type 'easy' or 'hard':").lower()
if difficulty_level=="hard":
    lifes=5
elif difficulty_level=="easy":
    lifes=10
#def match_the_number(lfs,nbr):
while runloop==True:
    print(f"You have {lifes} attempts remaining to guess the number.")
    guessed_number=int(input("Make a guess: "))
    if guessed_number==number:
        print(f"You got it! The answer was {number}.")
        runloop = False
    elif lifes==0:
        print("You've run out of guesses, you lose.")
        runloop = False
    elif number>guessed_number:
        print("Too Low, try again")
        lifes-=1
    elif number<guessed_number:
        print("Too high, try again")
        lifes-=1