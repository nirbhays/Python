#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
TotalBill=float(input ("What is the total amount of bill? " ))
TotalPayers=int(input ("How many of us are together ? " ))
TotalTip=int(input ("How much percentage of tip we want to give 10, 12 or 15 %? " ))
tipValue=(TotalTip/TotalBill)*100
totalpyableBill=tipValue+TotalBill
billforeach=round(totalpyableBill/TotalPayers,2)
print( f"Each of us have to pay : {billforeach}")