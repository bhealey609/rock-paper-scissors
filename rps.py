from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0, 2)]

player = False

while player == False:
    player = input("Rock, paper, or scissors?")
    if player.lower() == computer.lower():
        print("Tie!")
    elif player.lower() == "rock":
        if computer.lower() == "paper":
            print("You lose!", computer, "covers", player.lower())
        else:
            print("You win!", player, "smashes", computer.lower())
    elif player.lower() == "paper":
        if computer.lower() == "scissors":
            print("You lose!", computer, "cut", player.lower())
        else:
            print("You win!", player, "covers", computer.lower())
    elif player.lower() == "scissors":
        if computer.lower() == "rock":
            print("You lose!", computer, "smashes", player.lower())
        else:
            print("You win!", player, "cut", computer.lower())
    else:
        print("Invalid play. Check your spelling.")
    player = False
    computer = t[randint(0, 2)]








