def blackjack():
    import random 
    from art import logo
    from replit import clear
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


    def draw_card():
        return random.choice(cards)

    def draw_card_user():
        card = draw_card()
        if card == 11 and (user_cards_sum + card) >21:
            card = 1
        return card


    def draw_card_computer():
        card = draw_card()
        if card == 11 and (computer_cards_sum + card) >21:
            card = 1
        return card


    def user_sum():
        return sum(user_cards)

    def computer_sum():
        return sum(computer_cards)

    def restart():
        restart = input('Would you like to play again?')
        if restart == "yes" : 
            clear()
            blackjack()
        else:
            print("thanks for playing")

    print("Welcome to the ROYAL BLACKJACK")

    
    user_cards = []
    user_cards.append(draw_card_user())
    user_cards.append(draw_card_user())
    user_cards_sum = user_sum()
    print(f"Your cards are {user_cards}")
    print(f"The sum of your cards is {user_cards_sum}")

    computer_cards = []
    computer_cards.append(draw_card_computer())
    computer_cards_sum = computer_sum()
    print(f"The Dealer deals an {computer_cards}")



    user_choice = input('Would you like to hit or fold?\n')

    while user_choice == 'hit':
        if user_choice == 'hit' :
            user_cards.append(draw_card_user())
            user_cards_sum = sum(user_cards)
            print(user_cards)
            if user_cards_sum > 21:    
                print("you lose")
                print(f"sum: {user_cards_sum}")
                restart()

            else : 
                print(f"sum: {user_cards_sum}")
                user_choice = input('Would you like to hit or fold?\n')
        
    else:
        computer_total = computer_sum()

        while computer_total < 21 : 
            computer_cards.append(draw_card_computer())
            print(f'the dealer draws{computer_cards}')    
            computer_total = computer_sum()
            if computer_total == user_cards_sum :
                print("It's a draw")
                restart() 

        user_total = user_sum()
        if computer_total > 21 : 
            print(f'the sum of dealer is {computer_total}')
            print('You win')
            restart()
        

        if user_total > computer_total :
            print(f'Your total is {user_total} and dealer total is {computer_total}')
            print('You win')
            restart()
        else : 
            print(f'Your total is {user_total} and dealer total is {computer_total}')
            print('You lose')
            restart()

blackjack() 
