v = 0
c = 0
d = 0
e = 0
m = 0
t = 0
b = 30000.00
loop = 0
print('Enter the price of each category of expense.')
while loop != 5:
    if loop == 0:
        vi = input('Venue: ')
        try:
            v = float(vi) # if user inputs any non-number, ValueError
            if 0 > v: # if user inputs a negative, throw error
                raise Exception # used to throw negnum error
        except ValueError:
            print('Please input a number.')
        except Exception: # we also catch it so we will keep looping even with this
            print("Please enter 0 or a positive number.")
        else:
            loop += 1 # increment loop
    if loop == 1:
        ci = input('Catering: ')
        try:
            c = float(ci)
            if 0 > c:
                raise Exception
        except ValueError:
            print('Please input a number.')
        except Exception:
            print("Please enter 0 or a positive number.")
        else:
            loop += 1
    if loop == 2:
        di = input('Decorations: ')
        try:
            d = float(di)
            if 0 > d:
                raise Exception
        except ValueError:
            print('Please input a number.')
        except Exception:
            print("Please enter 0 or a positive number.")
        else:
            loop += 1
    if loop == 3:
        ei = input('Entertainment: ') # EI EI MUUUUUUUUUUUUUN
        try:
            e = float(ei)
            if 0 > e:
                raise Exception
        except ValueError:
            print('Please input a number.')
        except Exception:
            print("Please enter 0 or a positive number.")
        else:
            loop += 1
    if loop == 4:
        mi = input('Miscellaneous: ')
        try:
            m = float(mi)
            if 0 > m:
                raise Exception
        except ValueError:
            print('Please input a number.')
        except Exception:
            print("Please enter 0 or a positive number.")
        else:
            loop += 1
t += v # this could've been one line but the assignment wants this so...
t += c
t += d
t += e
t += m
if t < b or t == b:
    print('Expenses are within budget.')
elif t > b:
    print('Expenses exceeds the budget.')