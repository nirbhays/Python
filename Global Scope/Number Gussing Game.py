from random import randint
import art
print(art.logo)
def guess_number():
    print("I'm thinking of a number between 1 and 100")
    number = randint(1, 100)
    runloop = True
    difficulty_level=input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if difficulty_level=="hard":
        lifes=5
    elif difficulty_level=="easy":
        lifes=10
    while runloop==True:
        print(f"You have {lifes} attempts remaining to guess the number.")
        guessed_number=int(input("Make a guess: "))
        if guessed_number==number:
            print(f"You got it! The answer was {number}.")
            runloop = False
        elif lifes==1:
            print("You've run out of guesses, you lose.")
            runloop = False
        elif number>guessed_number:
            print("Your number is too low, try again")
            lifes-=1
        elif number<guessed_number:
            print("Your number is too high, try again")
            lifes-=1
runagain=(input(" Do you want to play the Game, Yes or No? :")).lower()
while runagain=="yes":
    guess_number()