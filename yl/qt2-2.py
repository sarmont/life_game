import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    # Создание курсора
    cur = con.cursor()
    cur.execute("""
    update films 
    set duration = 42
    where duration = ''''
    """).fetchall()
    con.commit()
    con.close()


bd = input()
get_result(bd)
