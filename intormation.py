import sqlite3

db_name = 'information.db'
conn = None
cursor = None


def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


def close():
    cursor.close()
    conn.close()


def do(query):
    cursor.execute(query)
    conn.commit()


def clear_db():
    open()
    query = '''DROP TABLE IF EXISTS military'''
    do(query)
    close()


def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')

    do("""CREATE TABLE IF NOT EXISTS military(
    Name TEXT,
    Surname TEXT,
    Birthday_year INTEGER,

    Rank TEXT,
    Type_of_army TEXT,
    Awards TEXT,
    Place_of_duty TEXT);""")

    close()



def add_peoples():
    peoples = [('Барсик', 'Ч', 2000, 'Вісловухий', 'В Маріуполі', 'Британський короткошерстний', '22 роки та 2 місяці'),
               ('Корашка', 'Ж', 2022, 'В чорнобілих плямках', 'село "Сеньківка"', 'Шиншилка', '7 місяців'),
               ('Наомі', 'Ж', 2020, 'Жовта, як сонце', 'Київська область', 'Мейн-кун', '1 рік 6 місяців'),
               ('Хлібчик', 'Ч', 2018, 'Колір шерсті світло-коричневий', 'В Бердичеві', 'Сіамський кіт', '4 роки 5 місяців'),
               ('Пискля', 'Ч', 2022, 'Кожен "мяу" виходить писклявим', 'В Одесі', 'Корат', '7 місяців'),
               ('Уолтер', 'Ч', 2009, 'коли лежить завжди складає ручки(який діловий)', 'в  Карпатах', 'Регдолл', '13 років 1 місяць'),
               ('Матрос', 'Ч', 2017, 'В біло-чорних полосках', 'В Львові', 'Кінкалоу', '5 років'),
               ('Зорро', 'Ч', 2012, 'Маска на очах', 'В Донецькі', 'Тойгер', '10 років 1 місяць'),
               ('Кнопка', 'Ж', 2014, 'На спині чорна пляма', 'В Житомері', 'Сфінкс', '8 років 3 місяці'),
               ('Соня', 'Ж', 2021, 'Любить поспати', 'В Києві', 'Рагамаффін', '1 рік')]
    open()
    cursor.executemany("INSERT INTO military VALUES(?, ?, ?, ?, ?, ?, ?);", peoples)
    conn.commit()
    close()


def show():
    open()
    list1 = []
    cursor.execute("SELECT Name,Surname,Birthday_year FROM military;")
    for i in cursor.fetchall():
        print(i)
        list1.append(i)
    close()
    return list1


def get_question_after(name, surname, age):
    open()
    query = '''
    SELECT * FROM military WHERE Name == ?
    AND Surname == ? AND Birthday_year == ?'''
    cursor.execute(query, [name, surname, age])
    result = cursor.fetchone()
    close()
    return result


def main():
    clear_db()
    create()
    add_peoples()
    show()

main()