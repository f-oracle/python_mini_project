name = raw_input("Type your name: ")  # type: ignore
print('Welcome", name, "to this adventure!')

answer = raw_input(  # type: ignore
    "You are on a dirt road, it has come to an end and you can go left or right.  which way will you like to go question? ").lower()
if answer == "left":
    answer = raw_input(  # type: ignore
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")
    if answer == "swim":
        print("You swim accross you get eaten by an alligator.")

    elif answer == "walk":
        print("You walked for many miles, you ran out of water and you loose the game.")

    else:
        print("You choose the wrong option, you loose.")

elif answer == "right":
    answer = raw_input( # type: ignore
        "you have come to a bridge, it looks wobbly, do you want to cross it or head back? (cross or back) ")  # type: ignore
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer= raw_input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ") # type: ignore
        if answer == "yes":
            print("You talk to the stranger and they give you gold, You WIN!")
        elif answer == "no":
            print("You ignored the stranger, they are offended and you lose. ")
        else:
            print('Not a valid option, you lose')
    else:
        print("You choose the wrong option, you lose.")
else:
    print('Not a valid option, You lose')
