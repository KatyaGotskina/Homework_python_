from right_data import data

while True:
    try:
        day, month, year = list(map(int, input('Введите дату: ').split('.')))
        print(data(day, month, year))

    except Exception as err:
        print('Ваша ошибка: ', err)
 