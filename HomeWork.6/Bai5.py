from turtle import*
def draw_star(x,y, length):
    penup()
    forward(x)
    left(90)
    forward(y)
    right(90)
    pendown()
    for i in range(5):
        right(144)
        forward(int(length))

