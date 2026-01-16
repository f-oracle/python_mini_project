import random

user_wins = 0
computer_wins = 0
options = ["Rock", "Paper", "Scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q or quiet ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    #rock:0 paper:0 #scissors
    computer_picks = options[random_number]
    print("Computer picked" , computer_picks + ".")

    if user_input == "rock" and computer_pick == "scissors":
     print("You won!")
     user_wins += 1

print("Goodbye!")
