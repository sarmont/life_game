import random
import turtle

vasya = turtle.Turtle()

vasya.speed(100)
for i in range(1000):
    q = random.randint(10, 150)
    w = random.randint(1, 7)
    c = random.choice(['red', 'blue', 'black', 'yellow'])

    vasya.width(w)
    vasya.color(c)
    vasya.circle(q)

    # повернуться на случайный угол
    # проити вперед на случайное число шагов

