lo1 = True
lo2 = True
warn = False

dept = input('Please enter departure location: ')
dest = input('Please enter destination: ')
med = input('Please enter method of transportation: ')
while lo1 == True:
    dist = input('Please enter distance to travel in kilometers: ')
    try:
        distf = float(dist)
    except ValueError:
        print("Input isn't a number. Please retry.")
    else:
        lo1 = False
while lo2 == True:
    spd = input('Please enter travel speed in in kilometers per hour: ')
    try:
        spdf = float(spd)
    except ValueError:
        print("Input isn't a number. Please retry.")
    else:
        lo2 = False
print()
print('Departure Location:', dept)
print('Destination:', dest)
print('Method of Transportation:', med)
time = distf/spdf
disp = f"Travel time (hours): {time:.2f}"
print(disp)
if time > 5.0:
    warn = True
if warn == True:
    print('Travel time is greater than 5 hours, a rest stop is recommended to prevent fatigue.')