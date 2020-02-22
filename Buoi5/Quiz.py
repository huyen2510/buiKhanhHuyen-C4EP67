quiz = [
    {
    'question': 'Con nhen co bao nhieu chan',
    'choices': [
        '3 chan',
        '2 chan',
        '4 chan',
        '8 chan'
    ],
    ' right_ans' : 3
    },
    {
        'question': 'Con cho co bao nhieu chan',
        'choices': [
        '2 chan',
        '2 chan',
        '4 chan',
        '8 chan'
    ],
    ' right_ans' : 0
    }
]
for quizz in quiz:
    print(quizz['question'])
    choices = quizz['choices']
    for i in range (len(choices)):
        print(f'{i+1}.{ choices[i]}') #string format
    user_choice = int(input(' Tra loi: ')) - 1
    if user_choice == quizz[' right_ans']:
        print(" Nice!")
    else:
        print(" Sai Roi")

# for j in range(len(quiz)): 
#     print(quiz[j]['question'])
#     choices = quiz[j]['choices']
#     for i in range (len(choices)):
#         print(f'{i+1}.{ choices[i]}') #string format
#     user_choice = int(input(' Tra loi: ')) - 1
#     if user_choice == quiz[j][' right_ans']:
#         print(" Nice!")
#     else:
#         print(" Sai Roi")