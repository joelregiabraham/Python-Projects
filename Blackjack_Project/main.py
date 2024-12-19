import random
from art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(usr_score, com_score):
    if usr_score == com_score:
        return "Draw"
    elif com_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif usr_score == 0:
        return "Win with a Blackjack 😎"
    elif usr_score > 21:
        return "You went over. You lose 😭"
    elif com_score > 21:
        return "Opponent went over. You win 😁"
    elif usr_score > com_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):  #just run the loop 2 times, every time the loop runs, we get a new card
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Debugging
        print(f"Your Cards: {user_cards}, Current Score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        print(f"Computer Cards: {computer_cards}, Current Score: {computer_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, and final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, and final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play the game of BlackJack ? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()