import random

control = True
pl = ""
rl = False
score = 0
tie = 0
loss = 0
plo = False
pickset = ("rock", "paper", "scissors")

print("Let's play a small game of rock, paper, scissors!")
print("You know how to play right? Just pick one of the three!")
print("Ready? Just type your pick in! Let's go!")
print("Just type rock, paper, or scissors, no need to worry about capitalization.")
print("If you enter anything else, you'll have to re-enter with a valid choice.")
while control == True:
    while plo == False:
        pl = str(input("Now pick! ")).lower()
        if pl in pickset:
            cpu = random.choice(pickset)
            plo = True
        else:
            print("Hey, that's invalid. Pick again.")
    if (pl == "rock" and cpu == "paper") or (pl == "paper" and cpu == "scissors") or (pl == "scissors" and cpu == "rock"):
        print("Won! Nice one!")
        score = score + 1
    elif pl == cpu:
        print("Tied. That's close!")
        tie = tie + 1
    else:
        print("Lost... You gon' got!")
        loss = loss + 1
    print("Want to go again? Type yes or y to retry, type no or n to quit.")
    while plo == True:
        pl = str(input("Another round? ")).lower()
        if pl == "yes" or pl == "y":
            print("All right, one more!")
            pl = ""
            plo = False
        elif pl == "no" or pl == "n":
            print("See ya next time!")
            print("Score tally:")
            print("Wins: ", score)
            print("Ties: ", tie)
            print("Losses: ", loss)
            rl = True
            plo = False
        else:
            print("Invalid input. Make a proper response.")
    if rl == True:
        print("Thanks for playing!")
        control = False
print("Game closing...")