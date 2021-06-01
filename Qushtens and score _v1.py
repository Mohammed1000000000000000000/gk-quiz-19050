score = 0



#set of questions that are asked
#question 1
print("\nQuestion: 1|score:{}".format(score))
ans=input("What is the most famous song in the world?\na.shape of you\nb.Despasito\nc.closer \nYour answer : ")
if ans == 'shape of you' or ans == 'Shape of you' or ans =='A' or ans == 'a':
    print("Correct")
    score+=1
    print("Your score is",score)
else:
    print("Oops incorrect the correct answer is : shape of you" )
    if score <=0:
        score = 0
        print("Your score is",score)

print("\nQuestion: 1|score:{}".format(score))
ans=input("what is the most known anime seare in the world?\na Naruto..\nb.Pokemon\nc.Attack on Titan \nYour answer : ")
if ans ==  'Pokemon' or ans =='B' or ans == 'b':
    print("Correct")
    score+=1
    print("Your score is",score)
else:
    print("Oops incorrect the correct answer is : Pokemon ")
    if score <=0:
        score = 0
        print("Your score is",score)

print("\nQuestion: 1|score:{}".format(score))
ans=input("what is the mes popular movies of all timet?\na The Dark Knight\nb.Parasite\nc.Roma \nYour answer : ")
if ans == 'The Dark Knight' or ans =='A' or ans == 'a':
    print("Correct")
    score+=1
    print("Your score is",score)
else:
    print("Oops incorrect the correct answer is : The Dark Knight " )
    if score <=0:
        score = 0
        print("Your score is",score)
