score = 0

#Qushteans
Qa = 'What is the most famous song in the world?'
Qb = 'what is the most known anime seare in the world?'
Qc = 'what is the mes popular movies of all timet?'
#Ansers
Q1 = 'shape of you'
Q2 = 'Pokemon'
Q3 = 'The Dark Knight'
#set of questions that are asked
#question 1
#question 1
 
   #print("\nQuestion: 1|score:{}".format(score))
#Qushten1
print("Q1",Qa) 
ans=input("\na.shape of you\nb.Despasito\nc.closer \nYour answer : ")
if ans == 'shape of you' or ans == 'Shape of you' or ans =='A' or ans == 'a':
       print("Correct")
       score+=1
       print("Your score is",score)
else:
       print("Opes wrong answer the answer is :" ,Q1)
      
       if score <=0:
           score = 0
           print("Your score is",score)
#Qushten2
       print("Q2",Qb)
       ans=input("\na Naruto\nb.Pokemon\nc.Attack on Titan \nYour answer : ")
  
if ans == 'shape of you' or ans == 'Pokemon' or ans =='B' or ans == 'b':
       print("Correct")
       score+=1
       print("Your score is",score)
else:
       print("Opes wrong answer the answer is :" ,Q2)
       if score <=0:
           score = 0
           print("Your score is",score)
 #Qushtean3
print("Q3",Qc)
ans=input("\na The Dark Knight\nb.Parasite\nc.Roma \nYour answer : ")
if ans == 'shape of you' or ans == 'The Dark Knight' or ans =='A' or ans == 'a':
       print("Correct")
       score+=1
       print("Your score is",score)
else:
       print("Opes wrong answer the answer is :" ,Q3)
       if score <=0:
           score = 0
           print("Your score is",score)
 
 
