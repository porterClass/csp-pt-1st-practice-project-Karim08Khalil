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
    roll = roll_random(1, 102)
    if 1 <= roll <= 25:
        return "Hearts"
    elif 26 <= roll <= 50:
        return "Clubs"
    elif 51 <= roll <= 75:
        return "Diamonds"
    elif 76 <= roll <= 100:
        return "Spades"
    else:
        return "Joker"
    


#Number of card(Faces)
def card_face():
    roll = roll_random(1, 10)
    if roll == 1:
        return "Ace"
    elif 2 <= roll <= 9:
        face_values = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        return face_values[roll - 2]  
    else:
        return royal()  


#Special Cards
def royal():
    roll = roll_random(1, 4)
    if roll == 1:
        return "Ten"
    elif roll == 2:
        return "Jack"
    elif roll == 3:
        return "Queen"
    else:
        return "King"
    

#print statement of card choosen
def draw_card():
    face = card_face()
    suit = card_suit()
    if card_suit() == "Joker":
        print("You have drawn Joker!")
    else:
        print(f"You have drawn the {face} of {suit}.")

#MultipleDraws

#Calling the function

draw_card() 
draw_card()
draw_card()
draw_card()
draw_card()
