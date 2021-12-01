# function to check if the given year is leap year or not
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False

        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid Month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 'There are 29 days'
    else:
        return f"There are {month_days[month-1]} days"


# Get user input
year = int(input("Enter a year : "))
month = int(input("Enter a month : "))
days = days_in_month(year, month)
print(days)
