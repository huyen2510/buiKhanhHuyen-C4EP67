dictionary = {
    'G9' : ' Good night',
    'J4F' : 'Just for fun'
}

# input(" Ban muon tim nghia tu nao? ")
j = True
while j: 
    a = input(" Ban muon tim nghia tu nao? ")
    if a == 'G9' in dictionary:
        print(dictionary['G9'])
    elif a == 'J4F' in dictionary: 
        print(dictionary['J4F'])
    else:
        print(" Tu ban muon tim k co trong tu dien! ")
        b =input('Ban co the nhap nghia tu nay: ')
        dictionary[a] = b
        print(dictionary[a], ": ", b)
    c = input(" Ban co muon tiep tuc? 1 ='yes' 0 = 'no' ")
    if int(c) == 1 :
        j = True
    else: 
        j= False
