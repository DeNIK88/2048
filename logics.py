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

def move_left(mas):
    #1. Удалить все нули
    #2. Добавить нули справа
    #3. Сложить одинаковые цифры
    #4. Если сложить удалось добавить еще ноль

    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for row in range(4):
        for column in range(3):
            if mas[row][column] == mas[row][column+1] and mas[row][column] != 0:
                mas[row][column]*=2
                mas[row].pop(column+1)
                mas[row].append(0)
    return mas

def move_right(mas):
    #1. Удалить все нули
    #2. Добавить нули слева
    #3. Сложить одинаковые цифры
    #4. Если сложить удалось добавить еще ноль (слева)

    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for row in range(4):
        for column in range(3, 0, -1):
            if mas[row][column] == mas[row][column-1] and mas[row][column] != 0:
                mas[row][column]*=2
                mas[row].pop(column-1)
                mas[row].insert(0, 0)
    return mas



