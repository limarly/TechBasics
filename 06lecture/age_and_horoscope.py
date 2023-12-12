# Python3 code to calculate age in years
from datetime import date

input_date = input(date)

#user_day = input("Day:")
#user_month = input("Month:")
#user_year = input(("Year:"))

def calculateAge(born):
    today = date.today()
    try:
        birthday = born.replace(year=today.year)

    # raised when birth date is February 29
    # and the current year is not a leap year
    except ValueError:
        birthday = born.replace(year=today.year,
                                month=born.month + 1, day=1)

    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

def calculateSign():
    if (user_month == 1 and user_day < 19) or (user_month == 12 and user_day >= 22):
        user_sign = "capricorn"
    elif(user_month == 2 and user_day < 18) or (user_month == 1 and user_day <= 20):
        user_sign = "aquarius"
    elif (user_month == 3 and user_day < 19) or (user_month == 2 and user_day <= 20):
        user_sign = "pisces"
    elif(user_month == and user_day < 22) or (user_month == 1 and user_day <= 22):
        user_sign = "aquarius"
    elif (user_month == and user_day < 22) or (user_month == 1 and user_day <= 22):
        user_sign = "aquarius"
    elif (user_month == and user_day < 22) or (user_month == 1 and user_day <= 22):
        user_sign = "aquarius"
    elif (user_month == and user_day < 22) or (user_month == 1 and user_day <= 22):
        user_sign = "aquarius"

# Driver code
print(calculateAge(date(2000, 9, 21)), "years")




