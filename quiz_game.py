print('welcome to computer quiz!')

playing = raw_input("Do you want to play? ")  # type: ignore


if playing != "yes":
    quit()

print("okay! Let's play: )")
score = 0  # this will start checking all the scores for the quiz

answer = raw_input("what does CPU stand for? ")  # type: ignore
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1  # start adding 1 to all score if score correctly
else:
    print("incorrect")

answer = raw_input("what does GPU stand for? ")  # type: ignore
if answer.lower() == "graphic processing unit":
    print('correct!')
    score += 1
else:
    print("incorrect")

answer = raw_input("what does RAM stand for? ")  # type: ignore
if answer.lower() == "random access memory":
    print('correct!')
    score += 1
else:
    print("incorrect")

answer = raw_input("what does PSU stand for? ")  # type: ignore
if answer.lower() == "power supply":
    print('correct!')
    score += 1
else:
    print("incorrect")

print("You got " + str(score) + " questions correct!")  # sums all the score
print("You got " + str((score / 4) * 100) + "%.") # this adds % of the quiz
