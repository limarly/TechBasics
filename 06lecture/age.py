import os
from datetime import date

os.system(("clear"))

"""day = input("day ")
month = input("month ")
years = input("year ")

print(type(day))
print(type(month))
print(type(years))"""

dob = input("What is your date of birth? Please specify in the format - YYYY-MM-DD:")
print(type(dob))

# split the dob into year, month, day
year, month, day = dob.split("-")
year = int(year)
month = int(month)
day = int(day)


def calculate_age(year, month, day):
    # convert the dob into date format
    dob = date(year, month, day)

    # print("New dob:", dob)
    # print(type(dob))

    # todays date
    current_date = date.today()
    # print(type(current_date))

    # calculate the age
    user_age = int((current_date - dob).days / 365.25)

    return user_age

def calculate_horoscope(month, day):
    if (month == 1 and day < 19) or (month == 12 and day >= 22):
        user_sign = "capricorn"
    elif(month == 2 and day < 18) or (month == 1 and day <= 20):
        user_sign = "aquarius"
    elif (month == 3 and day < 19) or (month == 2 and day <= 20):
        user_sign = "pisces"
    elif(month == 4 and day < 22) or (month == 3 and day <= 22):
        user_sign = "aries"
    elif (month == 5 and day < 22) or (month == 4 and day <= 22):
        user_sign = "taurus"
    elif (month == 6 and day < 22) or (month == 5 and day <= 22):
        user_sign = "gemini"
    elif (month == 7 and day < 22) or (month == 6 and day <= 22):
        user_sign = "cancer"
    elif (month == 8 and day < 22) or (month == 7 and day <= 22):
        user_sign = "leo"
    elif (month == 9 and day < 22) or (month == 8 and day <= 22):
        user_sign = "virgo"
    elif (month == 10 and day < 22) or (month == 9 and day <= 22):
        user_sign = "libra"
    elif (month == 11 and day < 22) or (month == 10 and day <= 22):
        user_sign = "scorpius"
    elif (month == 12 and day < 22) or (month == 11 and day <= 22):
        user_sign = "sagittarius"

    return user_sign


user_age = calculate_age(year, month, day)
user_sign = calculate_horoscope(month, day)
print(f"The age is {user_age} and sign is {user_sign}")