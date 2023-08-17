# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1=name1.lower()
name2=name2.lower()
T=name1.count("t")
R=name1.count("r")
U=name1.count("u")
E=name1.count("e")
T2=name2.count("t")
R2=name2.count("r")
U2=name2.count("u")
E2=name2.count("e")
sum1=T+R+U+E+T2+R2+U2+E2
L=name1.count("l")
O=name1.count("o")
V=name1.count("v")
E12=name1.count("e")
L2=name2.count("l")
O2=name2.count("o")
V2=name2.count("v")
E22=name2.count("e")
sum2=L+O+V+E12+L2+O2+V2+E22
sum=sum1+sum2
OP=f"{sum1}{sum2}"
OP=int(OP)
if OP<10 or OP>90:
    print(f"Your score is {OP}, you go together like coke and mentos.")
elif OP>=40 and OP<=50:
    print(f"Your score is {OP}, you are alright together.")
else:
    print(f"Your score is {OP}.")