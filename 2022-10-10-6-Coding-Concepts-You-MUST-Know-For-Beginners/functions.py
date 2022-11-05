import datetime

def calculate_age(dateOfBirth):
    today = datetime.datetime.now()
    age = today.year - dateOfBirth.year - ((today.month, today.day) < (dateOfBirth.month, dateOfBirth.day))
    return age

def print_result(age):
    if age >= 18:
        print("You are " + str(age) + "! Enjoy the film")
    else:
        print("Sorry you aren't old enough you are only " + str(age))

dateOfBirth = datetime.datetime(1995, 9, 20)
age = calculate_age(dateOfBirth)

print_result(age)