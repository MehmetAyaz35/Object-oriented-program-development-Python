import random

game_actions = ["rock", "paper", "scissors"]
continue_game = 3
number_of_games = 0

while number_of_games < continue_game:
    computer_choice = random.choice(game_actions)
    print("rock, paper, scissors: ")
    player_choice = input("Which action do you choose: ")
    print(f"You choose {player_choice}, computer choise {computer_choice}")

    if player_choice in game_actions:
        if computer_choice==player_choice:
            print(f"Both players choose {computer_choice}, it is tie")
        elif computer_choice == "rock":
            if player_choice == "paper":
                print("Paper covers rock, you win")
            else:
                print("Rock smashes scissor, you lose")
        elif computer_choice == "paper":
            if player_choice == "rock":
                print("Paper covers rock, you lose")
            else:
                print("Scissors cuts paper, you win")
        elif computer_choice == "scissors":
            if player_choice == "paper":
                print("scissors cuts paper, you lose")
            else:
                print("Rock smashes scissors,you win")

        number_of_games += 1
    else:
        print("invalid, try again")



