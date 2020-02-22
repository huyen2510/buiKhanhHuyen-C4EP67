# age = 18
# name ='mai'
# if age >= 18 and name ='Mai': 
#     print(" welcom to")
# elif age==18:
#     print(" doi them nam nua ")
# else: 
#     print (" bo me em dau ")
# # if and/ or , elif,else 

a =int( input(" nhap a = "))
b =int( input(" nhap b = "))
c =int( input(" nhap c = "))
delta = b**2 -4 *a*c
print( "delta = ", delta)
if delta > 0:
    print(" nghiem thu nhat la",( -b + delta**0,5) /(2*a))
    print(" nghiem thu nhat la", (-b - delta**0,5) / (2*a))
# f = format 
# print(f"x1= {x1} x2 = {x2}")
elif delta == 0 :
    print ("nghiem kep la:" , -b/(2*a) )
else: 
    print(" phuong trinh vo nghiem")

