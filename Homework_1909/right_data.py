"""Checks date."""


def data_check(our_data: str):
    """Takes date and checks if the date exists.

    Args:
        our_data: str - date like 01.02.2005.

    Returns:
         bool :  True if the date exists and False if not.
    """
    day, month, year = list(map(int, our_data.split('.')))
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    hundred = 100
    doesnt_exist = 13

    if year % 4 == 0 and year % hundred != 0 or year % (hundred * 4) == 0:
        days_in_month[1] = 29

    if 0 < month < doesnt_exist:

        return 0 < day <= days_in_month[month - 1]

    return False
