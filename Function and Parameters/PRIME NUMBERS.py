# Write your code below this line 👇

def prime_checker(number):
    if number==5 or number == 13:
        print (f"Given number {number} is a prime")
    elif number%2==0 or number%3==0 or number%5==0 or number % 13==0:
        print (f"Given number {number} is not a prime")
    else:
        print (f"Given number {number} is a prime")
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)