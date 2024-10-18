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


#jokers
def draw_card():
    if roll_random(1, 100) <= 2:
        return "You have drawn a Joker!"

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
    print(f"You have drawn the {face} of {suit}.")

if __name__ == "__main__":
    draw_card()


#Draws
def draw_multiple_cards(num_draws):
    drawn_cards = []
    for _ in range(num_draws):
        face = card_face()
        suit = card_suit()
        card = f"{face} of {suit}"
        drawn_cards.append(card)
        print(f"You have drawn the {card}.")
    return drawn_cards

#Get 5 cards
if __name__ == "__main__":
    num_cards = 5
    drawn_cards = draw_multiple_cards(num_cards)
