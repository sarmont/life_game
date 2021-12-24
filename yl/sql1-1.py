import sqlite3

g = input()
# Подключение к БД
con = sqlite3.connect('Chinook_Sqlite.sqlite')

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
result = cur.execute("""
              select distinct
                    album.title
              from 
                    album 
              left join track on album.albumid = track.albumid    
              left join genre on genre.genreid = track.genreid 
              where genre.name = ?
              order by album.artistid, album.title        
                        """, (g,)).fetchall()

# print(result)
# Вывод результатов на экран
for elem in result:
    print(elem[0])

con.close()
