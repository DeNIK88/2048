from logics import *
import pygame
import sys
from database import get_best, cur, insert_result

def game_loop():
    global score, mas
    draw_interface(score)
    pygame.display.update()

    while is_zero_in_mas(mas) or can_movie(mas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                delta = 0
                if event.key == pygame.K_LEFT:
                    mas, delta = move_left(mas)
                elif event.key == pygame.K_RIGHT:
                    mas, delta = move_right(mas)
                elif event.key == pygame.K_UP:
                    mas, delta = move_up(mas)
                elif event.key == pygame.K_DOWN:
                    mas, delta = move_down(mas)
                score += delta
                font = pygame.font.SysFont("stxingkai", 70)
                pygame.draw.rect(screen, WHITE_COLOR, TITLE_RECTANGLE)
                if is_zero_in_mas(mas):
                    empty = get_empty_list(mas)  # Беру список пустых элементов
                    random.shuffle(empty)  # Перемешал перемешиваю его
                    random_num = empty.pop()  # Удалил и взял последний элемент с конца списка.
                    # Метод поп возвращает взятый элемент.
                    i, j = get_index_from_number(random_num)  # Получил индексы элемента из его номера
                    mas = insert_2_or_4(mas, i, j)  # Поставил на место взятого пустого элемента 2 или 4
                    print(f'Мы заполнили элемент под номером {random_num}')
                draw_interface(score, delta)
                pygame.display.update()
        print(USERNAME)  # Проверка что имя введено то которое было введено пользователем

    game_over()


def draw_intro():
    img = pygame.image.load("2048img.png")
    font = pygame.font.SysFont("stxingkai", 70)
    text_welcome = font.render("Welcome!", True, WHITE_COLOR)
    name = "Введите имя"
    is_find_name = False  # Флаг введённого имени.

    while not is_find_name:     # Пока имя не найдено
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:  # Если тип события = нажатая клавиша
                if event.unicode.isalpha():     # isalpha Вернёт True, если в строке хотя бы один символ и все символы
                    # строки являются буквами, иначе — False.
                    if name == "Введите имя":
                        name = event.unicode    # Стирает "Введите имя" и пишет нажатый символ
                    else:
                        name += event.unicode       # конкатенирует name с нажатой клавишей
                elif event.key == pygame.K_BACKSPACE:   # если стереть
                    name = name[:-1]    # name = name без послледнего символа (срез)
                elif event.key == pygame.K_RETURN:  # если энтер
                    if len(name) > 2:
                        global USERNAME
                        USERNAME = name
                        is_find_name = True
                        break


        screen.fill(BLACK_COLOR)    # Залить всё черным. Что бы текст из предыдущей строки ложился на чистый лист,
        # а не друг на друга
        text_name = font.render(name, True, WHITE_COLOR)
        rect_name = text_name.get_rect()  # Взять координаты текста (прямоугольник)
        rect_name.center = screen.get_rect().center  # Разместить текст по центру главного экрана
        screen.blit(img, [10, 10])
        screen.blit(text_welcome, (250, 80))
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK_COLOR)

def game_over():
    global USERNAME, mas, score
    img = pygame.image.load("2048img.png")
    font = pygame.font.SysFont("stxingkai", 60)
    font_record = pygame.font.SysFont("stxingkai", 50)

    text_game_over = font.render("Game over!", True, WHITE_COLOR)
    text_score = font_record.render(f"Вы набрали {score} очков", True, WHITE_COLOR)
    best_score = GAMERS_FROM_DATABASE[0][1]     # Беру лучший результат из базы данных, только очки
    if score > best_score:
        text_record = font_record.render("Рекорд побит", True, WHITE_COLOR)
    else:
        text_record = font_record.render(f"Рекорд не побит: {best_score}", True, WHITE_COLOR)
    insert_result(USERNAME, score)
    make_disicion = False
    while not make_disicion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    # restart game with name
                    make_disicion = True
                    init_const()
                elif event.key == pygame.K_RETURN:
                    # restart game without name
                    USERNAME = None
                    make_disicion = True
                    init_const()

        screen.fill(BLACK_COLOR)
        screen.blit(text_game_over, (250, 80))
        screen.blit(text_score, (30, 250))
        screen.blit(text_record, (30, 300))
        screen.blit(img, [10, 10])
        pygame.display.update()
    screen.fill(BLACK_COLOR)

def draw_top_gamers():
    font_top = pygame.font.SysFont("simsun", 30) # Шрифт счетчика
    font_gamer = pygame.font.SysFont("simsun", 24) # Шрифт счетчика
    text_head = font_top.render("Best tries: ", True, COLOR_SCORE)
    screen.blit(text_head, (270, 5))
    for index, gamer in enumerate(GAMERS_FROM_DATABASE):
        # print(index, gamer)
        name, score = gamer
        # print(index+1, name, score)
        s = f"{index+1}. {name} - {score}"
        text_gamer = font_gamer.render(s, True, COLOR_SCORE)
        screen.blit(text_gamer, (270, 30 + index*30))


def draw_interface(score, delta=0):
    pygame.draw.rect(screen, WHITE_COLOR, TITLE_RECTANGLE) # Прямоугольник для игры

    font_score = pygame.font.SysFont("simsun", 48) # Шрифт счетчика
    text_score = font_score.render("Score: ", True, COLOR_SCORE) # Рисовка счетчика
    screen.blit(text_score, (20, 35)) # разместил счетчик
    text_score_value = font_score.render(f"{score}", True, COLOR_SCORE) # Рисовка значения счетчика
    screen.blit(text_score_value, (180, 35)) # разместил значение счетчика
    font_delta = pygame.font.SysFont("simsun", 32) # Шрифт счетчика2,  сколько прибавилось за ход

    font = pygame.font.SysFont("stxingkai", 70) # Шрифт цифр

    if delta > 0:
        text_delta = font_delta.render(f"+{delta}", True, COLOR_SCORE)  # Рисовка счетчика2
        screen.blit(text_delta, (175, 65))  # разместил значение счетчика2
    pretty_print(mas)
    draw_top_gamers()
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


def init_const():
    global score, mas
    mas = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    score = 0
    empty = get_empty_list(mas)  # Беру список пустых элементов
    random.shuffle(empty)  # Перемешал перемешиваю его
    random_num1 = empty.pop()  # Удалил и взял последний элемент с конца списка.
    # Метод поп возвращает взятый элемент.
    random_num2 = empty.pop()
    x1, y1 = get_index_from_number(random_num1)  # Получил индексы элемента из его номера
    mas = insert_2_or_4(mas, x1, y1)  # Поставил на место взятого пустого элемента 2 или 4
    x2, y2 = get_index_from_number(random_num2)
    mas = insert_2_or_4(mas, x2, y2)

mas = None
score = None
init_const()
COLOR_SCORE = (255, 127, 0)
COLORS = {
    0: (130, 130, 130),
    2: (130, 255, 255),
    4: (255, 130, 255),
    8: (255, 255, 130),
    16: (255, 255, 255),
    32: (0, 255, 255),
    64: (255, 0, 255),
    128: (255, 255, 0),
    256: (0, 130, 255),
    512: (130, 0, 255),
    1024: (130, 255, 0)
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
GAMERS_FROM_DATABASE = get_best()
USERNAME = None

print(get_empty_list(mas))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

while True:
    if USERNAME is None:
        draw_intro()
    game_loop()
    game_over()

