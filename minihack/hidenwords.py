# [OPTIONAL] Implement Word Jumble game
import random
words = ['rainbow', 'computer', 'science']
br = 0
while br != 3:
    a = random.choice(words)
    print(a)
    random_word = random.sample(a, len(a)) 
    ranw = ','.join(random_word)
    print("jumbled word is :", ranw) 
    ans = input("Tu ban doan la: ") 
    print(ans)
    if ans == a:
        print( " Correct!")
        br = 3
    else:
        print(" Incorrect")


