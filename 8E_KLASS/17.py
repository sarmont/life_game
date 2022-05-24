import turtle

v = turtle.Turtle()

def vanya():
    for i in range(4):
        v.fd(100)
        v.rt(90)
    v.rt(90)
    v.fd(100)
    v.lt(90)
    v.fd(50)
    v.circle(50)

vanya()
v.rt(300)
v.fd(50)
vanya()





input()