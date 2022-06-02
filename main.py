import random
while True:

    choices = ["rock", "paper", "scissors"]

    CPU = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == CPU:
        print("CPU: " ,CPU)
        print("player: ", player)
        print("Tie!")

    elif player == "rock":
        if CPU == "paper":
            print("CPU: " ,CPU)
            print("player: ", player)
            print("You lose!")
        if CPU == "scissors":
            print("CPU: " ,CPU)
            print("player: ", player)
            print("You win!")

    elif player == "paper":
        if CPU == "scissors":
            print("CPU: " ,CPU)
            print("player: ", player)
            print("You lose!")
        if CPU == "rock":
            print("CPU: " ,CPU)
            print("player: ", player)
            print("You win!")

    elif player == "scissors":
        if CPU == "paper":
            print("CPU: " ,CPU)
            print("player: ", player)
            print("You win!")
        if CPU == "rock":
            print("CPU: " ,CPU)
            print("player: ", player)
            print("You lose!")

    play_again = input("PLay again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye!")
