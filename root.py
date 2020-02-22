
from getpass import getpass
username = 'mindx'
password = 'xdmin'

loop = True

count  = 0
while loop :
    count = count + 1
    print(count)
    if count == 7 :
        print(" spam ")
        loop = False
    else:
        input_username = input('username?')
        if input_username == username:
            input_password = getpass()
            if input_password  == password:
                print(" wel to mindx")
                loop = False
            else:
                print(" wrong password")
        else:
            print(" wrong username")
