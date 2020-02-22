def calc(a, b, operator) :
    if operator == '+':
        result = a+b
    elif operator==" -":
        result = a- b
    elif operator == '*':
        result = a*b
    elif operator =="/":
        result = a/b
    return result
# function
if __name__ =='_main_' :
    a = calc(3,5,'+')
    print(a)