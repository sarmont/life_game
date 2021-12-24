import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    # Создание курсора
    cur = con.cursor()
    cur.execute("""
    update films 
    set duration = duration * 2
    where genre = (
            select id from genres where title = 'фантастика'
    )
    """).fetchall()
    con.commit()
    con.close()


bd = input()
get_result(bd)
