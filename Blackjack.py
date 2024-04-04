import os
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def deal(deck):
  hand = []
  for i in range(2):
     random.shuffle(deck)
     card = deck.pop()
     if card == 11: card = "J"
     if card == 12: card = "Q"
     if card == 13: card = "K"
     if card == 14: card = "A"
     hand.append(card)
  return hand

def total(hand):
  total = 0
  for card in hand:
    if card == "J" or card == "Q" or card == "K":
      total += 10
    elif card == "A":
      if total >= 11: total += 1
      else: total += 11
    else:
      total += card
  return total

def hit(hand):
   card = deck.pop()
   if card == 11: card = "J"
   if card == 12: card = "Q"
   if card == 13: card = "K"
   if card == 14: card = "A"
   hand.append(card)
   return hand
  
def play_again():
   again = input("Do you want to play again? (Y/N) : ")
   if again == "y":
        playerHand = []
        DealerHand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()
   else:
        print("Bye!")
        exit()

def clear():
   if os.name == 'nt':
      os.system('CLS')
   if os.name == 'posix':
      os.system('clear')

def results(playerhand, dealerhand):
   clear()
   print (f"Dealer has {dealerhand} for total of {total(dealerhand)} \n You have {playerhand} for a total of {total(playerhand)}")

def score(playerhand, dealerhand):
   if total(playerhand) == 21:
      print(f"Congratulations, You got Blackjack\n You got {total(playerhand)} \n Dealer got {total(dealerhand)}")
   elif total(dealerhand) == 21: 
      print(f"You lose, Dealer got Blackjack\n You got {total(playerhand)} \n Dealer got {total(dealerhand)}")
   elif total(playerhand) > 21:
      print(f"You busted, Dealer Wins\n You got {total(playerhand)} \n Dealer got {total(dealerhand)}")
   elif total(dealerhand) > 21:
      print(f"Dealer busted, You win \n You got {total(playerhand)} \n Dealer got {total(dealerhand)}")
   elif total(dealerhand) > total(playerhand):
      print(f"Dealer wins, you lose\n You got {total(playerhand)} \n Dealer got {total(dealerhand)}")
   elif total(dealerhand) < total(playerhand):
      print(f"You win!! \n You got {total(playerhand)} \n Dealer got {total(dealerhand)}")
    

def game():
  choice = ""
  playerIn = True
  dealerIn = True
  clear()
  print(f"WELCOME TO BLACKJACK!\n")
  DealerHand = deal(deck)
  playerHand = deal(deck)
  while choice !="q":
     while playerIn or dealerIn:
      print (f"The dealer is showing {DealerHand[0]} AND X")
      print (f"You have {playerHand[0]}, {playerHand[1]} for a total of {total(playerHand)}")
      if playerIn:
        choice = input(f"Do you want to Hit, Stand or Quit: ")
        clear()

        if choice == 's':
          playerIn = False
          while total(DealerHand) < 21:
            hit(DealerHand)
            print(f"Dealars hand: {DealerHand}")
            print(f"Your hand {playerHand}")
            if total(playerHand) > 21:
              print(f"You busted, Dealer wins \nYou have: {total(playerHand)} \nDealer got: {total(DealerHand)}")
              play_again

          score(playerHand, DealerHand)
          play_again()
        elif choice == 'h':
          hit(playerHand)
          while total(DealerHand) < 21:
            hit(DealerHand)
            print(f"Dealars hand: {DealerHand}")
            print(f"Your hand {playerHand}")
            if total(DealerHand) > 21:
              print(f"Dealer busted! You win \n You have: {total(playerHand)} \n Dealer got: {total(DealerHand)}")
              play_again
            
          score(playerHand, DealerHand)
          play_again()
          
        elif choice == 'q':
           print ("Bye!")
           exit
        else:
           print(f"You need to click h, s OR q to continue")

if __name__ == "__main__":
   game()