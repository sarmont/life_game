import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    # Создание курсора
    cur = con.cursor()
    cur.execute("""
    delete from films where genre = (
        select id from genres where title = 'комедия')
    """).fetchall()
    con.close()


bd = input()
get_result(bd)
