from logics import *
import pygame
import sys

def draw_interface():
    font = pygame.font.SysFont("stxingkai", 70)
    pygame.draw.rect(screen, WHITE_COLOR, TITLE_RECTANGLE)
    pretty_print(mas)
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]  # Вместе с отрисовкой квадратов узнаю значение по этому индексу
            text = font.render(f'{value}', True, BLACK_COLOR)
            w = column * BLOCK_SIZE + (column + 1) * MARGIN  # Точка  отрисовки квадрата по высоте
            h = row * BLOCK_SIZE + (row + 1) * MARGIN + 110  # По ширине
            pygame.draw.rect(screen, COLORS[value], (w, h, 110, 110))
            if value != 0:
                font_w, font_h = text.get_size()  # Узнал ширину и высоту текста
                text_x = w + (BLOCK_SIZE - font_w) // 2
                text_y = h + ((BLOCK_SIZE - font_h) // 2)
                screen.blit(text, (text_x, text_y))


mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 130),
    8: (255, 255, 0),
    16: (255, 130, 255)
}

color = (0, 0, 0)
BLACK_COLOR = (0, 0, 0)
GRAY_COLOR = (130, 130, 130)
WHITE_COLOR = (255, 255, 255)
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

draw_interface()
pygame.display.update()

while is_zero_in_mas(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            font = pygame.font.SysFont("stxingkai", 70)
            pygame.draw.rect(screen, WHITE_COLOR, TITLE_RECTANGLE)
            pretty_print(mas)
            empty = get_empty_list(mas)  # Получил список пустых элементов
            random.shuffle(empty)  # Перемешал список
            random_num = empty.pop()  # Удалил и взял последний элемент с конца списка.
            i, j = get_index_from_number(random_num)  # Получил индексы элемента из его номера
            mas = insert_2_or_4(mas, i, j)
            print(f'Мы заполнили элемент под номером {random_num}')
            draw_interface()
            pygame.display.update()
