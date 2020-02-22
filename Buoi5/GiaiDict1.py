teen_code = {
    'G9' : ' Good night',
    'J4F' : 'Just for fun'

}
loop = True
while loop: 
    word = input(" Nhap tu teencode ban muon tra: ").strip().lower()
    if word in teen_code:
        print(word, 'co nghia: ', teen_code[word])
    else:
        ans = input(" Tu tren khong co trong tu dien, ban co muon bo sung kh? (y/n)").lower()
        if ans == 'y':
            new_word = input(" Moi ban nhap vao tu do: ")
            teen_code[word] = new_word
        elif ans == 'n':
            print(" bye!")
            loop = False