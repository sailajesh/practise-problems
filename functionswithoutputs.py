'''formating name using title case() by function with output'''
def format_name(first_name,last_name):
    a=first_name.title()
    b=last_name.title()
    return f"{a} {b}"
full_name=format_name("sailajesh","saragadam")
print(full_name)

'''days in months'''


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


# TODO: Add more code here 👇
def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    leap_year = is_leap(year)

    if leap_year and month == 2:
        return 29

    return month_days[month - 1]

# 🚨 Do NOT change any of the code below
year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)

'''calling innerfunction'''

def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)

