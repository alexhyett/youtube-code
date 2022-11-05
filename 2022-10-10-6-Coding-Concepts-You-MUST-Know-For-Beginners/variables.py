import datetime

def calculate_age(dateOfBirth):
    today = datetime.datetime.now()
    age = today.year - dateOfBirth.year - ((today.month, today.day) < (dateOfBirth.month, dateOfBirth.day))
    return age

dateOfBirth = datetime.datetime(1990, 9, 20)
age = calculate_age(dateOfBirth)

print(age)