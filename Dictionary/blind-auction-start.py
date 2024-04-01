import os

#HINT: You can call clear() to clear the output in the console.
# Import the logo from art.py
import art as A
#os.system('cls')
#print(A.logo)

auction={}
player_dict={}
val=True
higest_bidder_value=0
winner=""
def higest_bidder(bidding_record):
    higest_bidder_value=0
    for bid in bidding_record:
        bidvalue=bidding_record[bid]
        if bidvalue>higest_bidder_value:
            higest_bidder_value=bidvalue
            winner=bid
    print(f"The winner is {winner}  with higest bid value of {higest_bidder_value} ")

goagain=""
while val==True:
    os.system('cls')
    print(A.logo)
    input_name = input("What is your name?: ").lower()
    input_bid = int(input("What's your bid?: $"))
    player_dict={ input_name: input_bid, }
    auction[input_name]=input_bid
    goagain = input("Do you have anyone else in the room?\n").lower()
    if goagain=="no":
        val=False
        higest_bidder(auction)
#autionbid(input_name,input_bid)
