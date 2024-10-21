#Karim Khalil
#Period 3rd
#October 25,2024

#Creating a random sequence
import random

#Random roll
def roll_random(low, high):
    return random.randint(low, high)



#Type of card
def card_suit():
    roll = roll_random(1, 100)
    if 1 <= roll <= 25:
        return "Hearts"
    elif 26 <= roll <= 50:
        return "Clubs"
    elif 51 <= roll <= 75:
        return "Diamonds"
    elif 76 <= roll <= 100:
        return "Spades"


#Getting a joker
def joker():
    num = roll_random(1, 100)
    if 1<= num <= 2:
       return "Joker"
    else: 
       return card_suit()

    


#Number of card(regular numbers)
def card_face():
    roll = roll_random(1, 10)
    if roll == 1:
        return "Ace"
    elif 2 <= roll <= 9:
        face_values = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        return face_values[roll - 2]  
    else:
        return royal()   


#Royal cards(special cards)
def royal():
    roll = roll_random(1, 4)
    if roll == 1:
        return "Ten"
    elif roll == 2:
        return "Jack"
    elif roll == 3:
        return "Queen"
    elif roll == 4:
        return "King"
    
    

#print statement of card choosen( drawing the cards)
def draw_card():
    if joker() == "Joker" :
        print("You have drawn Joker!")
    else:
        print("You have drawn the", card_face(), "of", card_suit() + ".")

#MultipleDraws

#Calling the function(5 times)

draw_card() 
draw_card()
draw_card()
draw_card()
draw_card()
