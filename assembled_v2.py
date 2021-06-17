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
['How many players are on a volleyball court?',
 {'answer':'d','option':'a.3\nb.6\nc.2\nd.12'}
 ],
['How many time zones are there in Russia?',
 {'answer':'a','option':'a.11\nb.13\nc.1\nd.10'}
 ],
['What’s the national animal of Australia?',
 {'answer':'a','option':'a.Red Kangaroo\nb.Dingo\nc.Platypus\nd.Rainbow Lorikeet'}
 ],
['Name the best-selling book series of the 21st century?',
 {'answer':'c','option':'a.Beloved\nb.The Great Gatsby\nc.Harry Potter\nd.Beloved'}
 ],
['Name the longest river in the world?',
 {'answer':'a','option':'a.The Nile\nb.Amazon Riverdel gkquiz[0]\nc.Paraná River\nd.Irtysh River'}
 ],
['How many stripes are there on the US flag?',
 {'answer':'c','option':'a.10\nb.12\nc.13\nd.20'}
 ],
['What’s the national flower of Japan?',
 {'answer':'a','option':'a.Cherry blossom\nb.Peony\nc.Orchid\nd.Lily'}
 ],
]

shuffle(gkquiz)


#Name Age 
print ("Welcome to the Quiz")

while True:
    name = input("what is your name : ")
    if name.replace(' ','').isalpha():
        break
    print("please enter characters A-Z onle")

def age():
    while True:
        age = input("\nPlease enter your age : ")
        if age.replace(' ','').isnumeric():#using replace to allow spaces after the answer
            if 6< int(age)<101: #allowing age till 7 to 100 only
                break
            else:
                print('You need to be 7 to 100')
        else:
            print("The data type you have used is invalid data type.\n")
#Rules
rule = input("Please enter y if you wamt to read the rules\nor any other key if you dont want to read :")

if rule ==  'Y' or rule  ==  'y' or  rule == 'Yes' or rule == 'yes':
    print("You will be given a question and Multiple ansers\nand you have to choose the right anser\nPlease answer the question with a,b,c or d and enjoy your time : ")
    
else:
    print("enjoy yor time")

#Ask if they are ready to take the quiz
status = input("Are you ready to take the quiz :{}?: \na. Yes \nb. No \n=>".format(name))

#What if the user is not ready
if status == 'No' or status == 'no' or status == 'n' or status == 'N': 
    print("See you next time.")
    exit()
    
#what if the user is ready
else:
    print("Welcome to the quiz.")

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

print("You have succesfully completed Mohammed's Game quiz!")
print(name,"Your final score is", score,"out of",total)
print("That means you answered", (round(score/total*100,2)),"% of the questions correctly!")
print("Thanks for playing")
exit()


      
