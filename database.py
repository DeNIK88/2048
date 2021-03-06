import sqlite3

bd = sqlite3.connect("2048.sqlite")  # Подключаю бд. В параметрах название и через точку формат бд.
cur = bd.cursor()
"""В информатике и технологии курсор базы данных представляет собой структуру управления, которая позволяет обходить 
записи в базе данных. Курсоры облегчают последующую обработку в сочетании с обходом, таким как извлечение, 
добавление и удаление записей базы данных. Курсор базы данных, характерный для обхода, делает курсоры похожими на 
концепцию итератора языка программирования. """

def insert_result(name, score):
    cur.execute("""
    insert into RECORDS values (?, ?)
    """, (name, score))
    bd.commit()

def get_best():
    cur.execute(
        """
    create table if not exists RECORDS (
    name text,
    score integer
    )""")
    # create table if not exists RECORDS - создать табличку если еще не создана с именем РЕКОРДС
    # name text - колонка найм, хранит текст
    # score integer - колонка скоре, хранит целое число
    cur.execute(
        """
    SELECT name, max(score) from RECORDS
    GROUP by name
    ORDER by score DESC
    limit 3"""
    )
# SELECT name, max(score) from RECORDS - выбрать (столбцы) нейм, скоре из РЕКОРДС
# Группировать по нейм, объединяет одинаковые нейм в один
# сортировать по скоре деск(от большего к меньшему)
# показать первые три строки

    return cur.fetchall()
# Вернуть записи в курсоре

insert_result('qwerty', 999)
