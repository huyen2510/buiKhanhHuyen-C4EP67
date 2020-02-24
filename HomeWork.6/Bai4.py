from turtle import*
from Bai3 import draw_square
# def draw_square(length, square_color):
#     # length =int( input(" Nhap độ dài: "))
#     # square_color = input(" Nhập màu: ")
#     color(square_color)
#     shape("turtle")

#     forward(length)
#     right(90)
#     backward(length)
#     right(90)
#     forward(length)
#     left(90)
#     forward(length)

#     mainloop()

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
