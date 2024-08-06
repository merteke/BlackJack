import random

card_deck=["ace","two","three","four","five","six","seven","eight","nine","ten","joker","queen","king"]

def deal_cards():
    hand=[]
    hand.append((random.choice(card_deck)))
    hand.append((random.choice(card_deck)))
    return hand

def give_card():
    return random.choice(card_deck)

def win_condition(player_score,computer_score):
    if player_score==21 and computer_score!=21:
        
        return True
        
        
    elif player_score==21 and computer_score==21:
        
        return True
        
    
    # elif player_score!=21 and computer_score==21:
        
    #     return True
        
    return False