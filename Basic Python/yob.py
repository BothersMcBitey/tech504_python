import datetime

age_int = input("How old are you (years): ")
name_str = input("What's your name? ")

yob = datetime.datetime.now().year - int(age_int)

print(f"OMG, you are {age_int} years old so you were born in {yob}")

hours_lived = float(age_int) * 365.25 * 24.0
print(f"You've lived for ~{hours_lived} hours")

def is_day_valid(day, month, year):
    if day < 1 or day > 31:
        return False
    if month == 2:
        if day > 29:
            return False
        # no one alive today was born in 1900 or earlier
        if (year % 4) != 0 and day > 28:
            return False
    if month in [4,6,9,11] and day == 31:
        return False
    return True

birth_month = int(input("Actually, which month were you born in (1-12)? "))
while birth_month < 1 or birth_month > 12:
    birth_month = int(input("That's not a real month. Try again (1-12)? "))

birth_day = int(input("And what day (1-31)? "))
while not is_day_valid(birth_day, birth_month, yob):
    birth_day = int(input("That day isn't valid. Try again (1-31)? "))

birth_datetime = datetime.datetime(year=int(yob), month=birth_month, day=birth_day)

hours_lived = (datetime.datetime.now() - birth_datetime).total_seconds() // 360

print(f"So you've lived more like {hours_lived} hours. Probably.")