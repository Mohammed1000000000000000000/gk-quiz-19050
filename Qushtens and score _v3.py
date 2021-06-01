from random import shuffle
gkquiz = [
['What is the most famous song in 2020?',
 {'answer':'c','option':'a.Despasito\nb.closer\nc.shape of you\nd.Roses'}
 ],
['what is the most known anime seare in 2020?',
 {'answer':'a','option':'a.Pokemon\nb.Naruto\nc.Attack on Titan\nd.Great Pretender'}
 ],
['what is the meost popular movies in 2020?',
 {'answer': 'b','option':'a.Parasite\nb.The Dark Knight\nc.Roma\nd.Beanpole'}
 ],
]

index = 0
score = 0
optnum = 0
total=10
j=""
while len(gkquiz)>0:
    data = gkquiz[0]
    j = data[0]
    data = data[1]
    answer = data['answer']
    option = data['option']
 
    print(j)
    print(option)
 
    while True:
         user_answer = input("Please enter you answer here : ").lower()
         if user_answer == 'a' or user_answer == 'b' or user_answer == 'c' or user_answer == 'd':
            if user_answer == answer:
                print("Good work")
                score += 1
                print("Your score is",score)
            else:
                print("The answer is  wrong the right answer is",answer)
                print("Your score is",score)

            del gkquiz [0]
            break
         else:
            print("Enter your answer in a,b,c,d")

print("")
exit()
            
