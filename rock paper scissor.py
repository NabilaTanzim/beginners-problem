import random

choices = ("rock", "paper", "scissor")
while True:
    x = input(">").lower()
    y = random.choice(choices)
    print(">" + y)
    if x == y:
        print("Tie")
    elif x == "rock" and y == "scissor":
        print("You win")
    elif x == "scissor" and y == "paper":
        print("You win")
    elif x == "paper" and y == "rock":
        print("You win")
    elif x == "exit":
        break
    else:
        print("I win")
