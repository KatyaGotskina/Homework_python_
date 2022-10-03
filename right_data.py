def data(day, month, year):

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        days_in_month[1] = 29

    if month > 0 and month < 13:

        return day > 0 and day <= days_in_month[month - 1]

    else:
        return False
