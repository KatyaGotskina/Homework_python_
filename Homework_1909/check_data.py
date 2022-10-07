"""date validation using module 'right_data'."""
from right_data import data_check

while True:
    try:
        day, month, year = list(map(int, input('Введите дату: ').split('.')))
        print(data_check(day, month, year))

    except Exception as err:
        print('Ваша ошибка: ', err)
