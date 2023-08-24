  #Password Generator Project
import random
import sys
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPass Generator!")
nr_letters= int(input("How many letters would you like in your Password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
easyPass=""
ShufflePass=[]
password=""
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for i in range (0, nr_letters):
    random_letter = random.choice(letters)
    easyPass+=str(random_letter)
for j in range (nr_symbols):
    random_symbol = random.choice(symbols)
    easyPass+=str(random_symbol)
for k in range (nr_numbers):
    random_number = random.choice(numbers)
    easyPass+=str(random_number)
print(easyPass)
for i in easyPass:
    ShufflePass.append(i)
random.shuffle(ShufflePass)
print(ShufflePass)
for l in ShufflePass:
    password+=l
print (password)    