import random

print("\n ---- WELCOME TO MY GAME ----")

while True:
    my_gameslist = ["rock", "paper", "scissors"]
    player = None
    computer = random.choice(my_gameslist)

    while player not in my_gameslist:
        player = input("ENTER YOUR CHOICE (rock, paper, scissors): ").strip().lower()

    if computer == player:
        print("Player:", player)
        print("Computer:", computer)
        print("Tie!!")
    elif player == "rock":
        if computer == "paper":
            print("Player:", player)
            print("Computer:", computer)
            print("You lose!!")
        elif computer == "scissors":
            print("Player:", player)
            print("Computer:", computer)
            print("You win!!")
    elif player == "paper":
        if computer == "rock":
            print("Player:", player)
            print("Computer:", computer)
            print("You win!!")
        elif computer == "scissors":
            print("Player:", player)
            print("Computer:", computer)
            print("You lose!!")
    elif player == "scissors":
        if computer == "rock":
            print("Player:", player)
            print("Computer:", computer)
            print("You lose!!")
        elif computer == "paper":
            print("Player:", player)
            print("Computer:", computer)
            print("You win!!")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "no":
        break

print("BYEE")