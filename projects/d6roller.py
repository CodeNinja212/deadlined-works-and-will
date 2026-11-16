import random

die = [1,2,3,4,5,6] # define the die
con = True # control for the loop
suc = 0 # define var
fail = 0 # define var
x = 0 # how many dies to roll

while con == True:
    print('How many dies? Minimum of 1. Type 0 to end program.')
    try:
        x = int(input()) # ask input
    except ValueError: # not a number? go here
        print('Please type a number.')
    else:
        if x == 0: # if 0 was input, go here, cut the loop, end the program
            print('Program closing.')
            con = False
        else:
            rolls = random.choices(die, k=x) # "from this list, pick from it x amount of times. dupes are ok."
            print('Rolls: ', rolls)
            for x in rolls:
                if x < 4:
                    fail += 1
                elif x == 4 or x == 5:
                    suc += 1
                elif x == 6:
                    suc += 2
            print('Successes: ', suc, ', Failures: ',fail)
            suc = 0
            fail = 0