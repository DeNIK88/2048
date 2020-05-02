import random


def pretty_print(mas):
    print("-"*10)
    for raw in mas:
        print(*raw)
    print("-"*10)


def get_empty_list(mas):
    number_from_index_list = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                number_from_index_list.append(get_number_from_index(i, j))

    return number_from_index_list


def get_number_from_index(i, j):
    return i * 4 + j + 1


def get_index_from_number(num):
    num -= 1
    return num//4, num%4


def insert_2_or_4(mas, i, j):
    if random.random() <= 0.75:
        mas[i][j] = 2
    else:
        mas[i][j] = 4
    return mas


def is_zero_in_mas(mas):
    for raw in mas:
        if 0 in raw:
            return True
    return False
