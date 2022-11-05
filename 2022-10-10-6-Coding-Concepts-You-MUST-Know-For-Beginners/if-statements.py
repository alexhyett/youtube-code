import datetime

dateOfBirth = datetime.datetime(1990, 9, 20)
today = datetime.datetime.now()

age = today.year - dateOfBirth.year - ((today.month, today.day) < (dateOfBirth.month, dateOfBirth.day))

print(age)
if age >= 18:
    print("Enjoy the film")
else:
    print("Sorry you aren't old enough")