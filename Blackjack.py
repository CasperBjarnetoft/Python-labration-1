import os
import random

# Array för att göra själva kortleken
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

# Funktion för att dela ut kort till datorn och spelare
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

# Funktion för att hålla koll på hur många kort som spelaren och datorn har i handen
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

# Funktion för att dela ut nytt kort antigen till spelare eller dator
def hit(hand):
   card = deck.pop()
   if card == 11: card = "J"
   if card == 12: card = "Q"
   if card == 13: card = "K"
   if card == 14: card = "A"
   hand.append(card)
   return hand

# Funktion för att kunna starta om spelet och spela flera rundor
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

# Nollställer terminal vid nytt spel
def clear():
   if os.name == 'nt':
      os.system('CLS')
   if os.name == 'posix':
      os.system('clear')

# Funktion för att visa resultat efter spelad runda
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
    
# Funktionen som köra själva spelet
def game():
  choice = ""
  playerIn = True
  dealerIn = True
  clear()
  print(f"WELCOME TO BLACKJACK!\n")
  DealerHand = deal(deck)
  playerHand = deal(deck)
  
  # While loop som håller koll att spela är igång till användare klickar på q för att avsluta
  while choice !="q":
     
     # while loop som håller koll om spelen vill ta ett nytt kort eller stanna
     while playerIn:
      print (f"The dealer is showing {DealerHand[0]} AND X")
      print (f"You have {playerHand[0]}, {playerHand[1]} for a total of {total(playerHand)}")

      # if funktion som håller kolla på de tra valen som användare har
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

# if funktion som håller koll när själva spelet ska köras
if __name__ == "__main__":
   game()