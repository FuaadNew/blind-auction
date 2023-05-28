from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
Continue = True
BidList = {}

  

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
      
  #for bidder in bidding_record:
    #bid_amount = bidding_record[bidder]
    #if bid_amount > max:
      #max = bid_amount
      #Winner = bidder
    
  

  
  
  

while Continue != False:
  Prompt1 = input("What is your name?: ")
  Prompt2 = int(input("What is your bid?: $"))
  BidList[Prompt1] = Prompt2

  Answer = input("Are there any other bidders? Type 'yes or 'no'.\n")
  
  if Answer == 'yes':
    Continue = True
    clear()
  else:  
    Continue = False
    find_highest_bidder(BidList)
    
        
          
        
      
    

    


