input("Welcome to our shop, what do you want (C, R, U, D)?" )
a = input("Welcome to our shop, what do you want (C, R, U, D)?" )
oursitems = [ "T-Shirt", "Sweater"]
if a == "R":
    # print(" Our items: T-Shirt, Sweater")
    print(oursitems)
    elif a == "C":
        input(" Enter new items : ")
        b = input(" Enter new items : ")
        oursitems.append(b)
        print(oursitems)
    elif a == "U":
        input("Update position" )
        pos = input("Update position" )
        input(" Enter new items : ")
        b = input(" Enter new items : ")
        oursitems.append(b)
        print(b)
    elif a ==" D" :
        input("Delete at position" )
        pos = input("Delete at position" )
        oursitems.append(b)
        print(b) 
        

        

        

