# #Посчитать процент строк, где больше заглавных букв
def str_procent(slova):
    str_1 = slova.split()
    count1 = 0

    for i in str_1:
        hiigh = 0
        for j in i:
            if j.isupper():
                hiigh += 1
        if hiigh / len(i) > 0.5:
            count1 += 1

    return round(count1 / len(str_1) * 100, 2)


