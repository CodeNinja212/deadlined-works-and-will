loop_one = False
loop_two = False
age = None
score = None
complete = None
none_cases = {"n", "none"}

name = input("Enter name: ")
while loop_one == False:
    in_age = input("Enter age: ")
    try:
        age = int(in_age)
    except ValueError:
        print("Please enter a number.")
    else:
        loop_one = True
print("Please enter student score from quiz. The maximum score is 20.")
print("Enter n or none (any case) if the student hasn't completed the quiz.")
while loop_two == False:
    in_status = input("Enter student score: ").lower().strip()
    if in_status in none_cases:
        complete = False
        loop_two = True
        break
    try:
        score = float(in_status)
    except ValueError:
        print("Please enter n, none, or a number.")
    else:
        complete = True
    finally:
        if score is not None and score >= 10.0:
            status = True
        elif score is not None and score < 10.0:
            status = False
        if complete == True:
            loop_two = True
print("Name:", name)
print("Age:", age)
if complete == True:
    print("Quiz Score:", score)
    if status == True:
        print("Student has passed.")
    elif status == False:
        print("Student has failed.")
elif complete == False:
    print("Student has not completed the quiz yet.")
print("Query complete.")