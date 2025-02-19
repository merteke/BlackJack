import random
from art import logo,cards_art
from cards_value import card_value
import os
from bj import deal_cards,give_card,win_condition
import time
cls=lambda:os.system('cls')


card_deck=["ace","two","three","four","five","six","seven","eight","nine","ten","joker","queen","king"]
print(logo)
print("Welcome to BlackJack!")

your_hand=[]
computer_hand=[]
balance=int(input("What is your total balance?:\n$"))
while True:
    print(f"Your balance:${balance}")
    your_hand.clear()
    computer_hand.clear()
    player_score=0
    computer_score=0
    bet=int(input("How much money you wish to bet:\n$"))
    balance-=bet
    your_hand=(deal_cards())
    
    computer_hand.append((give_card()))
    

    
    print('Dealers hand:')
    time.sleep(1)
    for card in computer_hand:
        computer_score+=card_value[card]
        
    print(" ".join(cards_art[card] for card in computer_hand))
    time.sleep(1)
    print('Your hand:')
    time.sleep(1)
    for card in your_hand:
        player_score+=card_value[card]
        # print(cards_art[card])
    print(" ".join(cards_art[card] for card in your_hand))
    
    time.sleep(1)
    if player_score==21 and computer_score!=21:
        computer_hand.append(give_card())
        for card in computer_hand:
            computer_score+=card_value[card]
        if computer_score==21:
            print(f'Your hand:{(" ".join(cards_art[card] for card in your_hand))}\nDealers hand:{" ".join(cards_art[card] for card in computer_hand)}')
            print("Draw!")
        else:
            print(f'Your hand:{(" ".join(cards_art[card] for card in your_hand))}\nDealers hand:{" ".join(cards_art[card] for card in computer_hand)}')
            print("Black Jack!")
            print(f"You win:${bet*2.5}")
            balance+=bet*2.5
            print(f"Your total balance:${balance}")
                
        
        ################
    else:    
        if not win_condition(player_score,computer_score):
            while True:
                hit_or_stand=input(f"Your hand {player_score} and dealers hand {computer_score}, 'hit' or 'stand'?\n")
                cls()
                if hit_or_stand=="hit":
                    your_hand.append(give_card())
                    time.sleep(1)
                    print (f"You get {card_value[your_hand[-1]]}")
                    if your_hand[-1]=="ace":
                        if player_score<=10:
                            player_score+=11
                        else:
                            player_score+=1
                    else:
                        player_score+=card_value[your_hand[-1]]
                    print(" ".join(cards_art[card] for card in your_hand))
                    if player_score>21:
                        cls()
                        print(" ".join(cards_art[card] for card in your_hand))
                        print(f"Your hand:{player_score}\nYou lost!")
                        print(f"You lost:${bet}")
                        print(f"Your total balance:${balance}")
                        break
                if hit_or_stand=="stand":
                    print(f"Lets see what dealer got!")
                    time.sleep(1)
                    while computer_score<=player_score:
                        computer_hand.append(give_card())
                        print (f"Dealer gets {card_value[computer_hand[-1]]}")
                        if computer_hand[-1]=="ace":
                            if computer_score<=10:
                                computer_score+=11
                            else:
                                computer_score+=1
                        else:
                            computer_score+=card_value[computer_hand[-1]]
                        print(" ".join(cards_art[card] for card in computer_hand))
                        time.sleep(1)
                        cls()
                        
                    if computer_score>21:
                        print(f'Your hand:{(" ".join(cards_art[card] for card in your_hand))}\nDealers hand:{" ".join(cards_art[card] for card in computer_hand)}')
                        time.sleep(1)
                        print(f'You win with {player_score}, Dealer is busted!:{computer_score} ')
                        print(f"You win:${bet*2}")
                        balance+=bet*2
                        print(f"Your total balance:${balance}")
                        break    
                    if player_score>computer_score:
                        print(f'Your hand:{" ".join(cards_art[card] for card in your_hand)}\nDealers hand:{" ".join(cards_art[card] for card in computer_hand)}')
                        time.sleep(1)
                        print(f"You win!\nYour hand:{player_score}     Dealer's hand:{computer_score}   ")
                        print(f"You win:${bet*2}")
                        balance+=bet*2
                        print(f"Your total balance:${balance}")
                        break    
                    elif player_score==computer_score:
                        print(f'Your hand:{" ".join(cards_art[card] for card in your_hand)}\nDealers hand:{" ".join(cards_art[card] for card in computer_hand)}')
                        time.sleep(1)
                        print(f"Push!\nYour hand:{player_score}     Dealer's hand:{computer_score}  ")
                        print(f"You get back your:${bet}")
                        balance+=bet
                        print(f"Your total balance:${balance}")
                        break
                    elif player_score<computer_score:
                        print(f'Your hand:{" ".join(cards_art[card] for card in your_hand)}\nDealers hand:{" ".join(cards_art[card] for card in computer_hand)}')
                        time.sleep(1)
                        print(f"You lost!\nYour hand:{player_score}     Dealer's hand:{computer_score}  ")
                        print(f"You lost:${bet}")
                        print(f"Your total balance:${balance}")
                        break
                   
    play_again=(input("Do you want to play again?(y/n)"))
    if play_again=="n":
        cls()
        print(f"Your total balance:${balance}")
        break





