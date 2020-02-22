import random
from random import randint
from Caculator import calc

a = randint(0,9)
b = randint(0,9)
operators = ['+','-','-','*','/','+']
operator = operators[randint(0,3)] #operator = choice(operators)
resutl = calc(a , b,operator) 
random_num = randint(-1,1)
display_result = resutl + random_num

print( f'{a} {operator} {b} = {display_result}')

choice = input( "T/F ")

if ( random_num == 0) :
    if choice == 'T':
        print('Đúng')
    else:
        print("Sai!")
else:
    if choice =='F':
        print(" Đúng")
    else:
        print("Sai")
# if random_num == 0 and choice=='T':
#     print()