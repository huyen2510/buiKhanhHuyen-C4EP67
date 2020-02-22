for i in range(1,201):
    if i % 2 == 0 :
        print("{:>5}".format(str(i)) ,end = " ")
        if i % 20 == 0: 
            print(" ")
