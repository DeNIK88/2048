from logics import *
import pygame
import sys

# План работ
# Положить в массив два значения
# Начал цикл игры:
#    ждать от пользователя команды
#    когда получим команду обработать массив
#    найти пустые клетки
#    если есть пустые клетки случайно выбрать одну из них
#    и положить туда 2 либо 4
#    если пустых клеток нет и нельзя двигать массив, игра закончена

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

GRAY = (130, 130, 130)
COLOR = (255, 255, 255)
BLOCKS = 4
MARGIN = 10
BLOCK_SIZE = 110
WIDTH = BLOCKS*BLOCK_SIZE + (BLOCKS+1)*MARGIN
HEIGHT = WIDTH + BLOCK_SIZE
TITLE_RECTANGLE = pygame.Rect(0, 0, WIDTH, BLOCK_SIZE)


mas[1][2] = 2
mas[3][0] = 4
print(get_empty_list(mas))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

while is_zero_in_mas(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            pygame.draw.rect(screen, COLOR, TITLE_RECTANGLE)
            for row in range(BLOCKS):
                for column in range(BLOCKS):
                    w = column * BLOCK_SIZE + (column+1) * MARGIN
                    h = row * BLOCK_SIZE + (row+1) * MARGIN + 110
                    pygame.draw.rect(screen, GRAY, (w, h, 110, 110))
            # input()
            empty = get_empty_list(mas)  # Получил список пустых элементов
            random.shuffle(empty)  # Перемешал список
            random_num = empty.pop()  # Удалил и взял последний элемент с конца списка.
            i, j = get_index_from_number(random_num)  # Получил индексы элемента из его номера
            mas = insert_2_or_4(mas, i, j)
            print(f'Мы заполнили элемент под номером {random_num}')
            pretty_print(mas)
        pygame.display.update()