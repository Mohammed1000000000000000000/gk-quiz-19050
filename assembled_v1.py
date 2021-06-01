gkquiz = [
['What is the most famous song in 2020?',
 {'answer':'c','option':'a.Despasito\n b.closer\n c.shape of you\n d.Roses'}],
['what is the most known anime seare in 2020?',
 {'answer':'a','option':'a.Pokemon\n b.Naruto\n c.Attack on Titan\n d.Great Pretender'}],
['what is the meost popular movies in 2020?',
 {'answer': 'b','option':'a.Parasite\n b.The Dark Knight\n c.Roma\n d. Beanpole'}],
['How many players are on a volleyball court?',
 {'answer':'d','option':'a.3\n b.6\n c.2\n d.12'}],
['How many time zones are there in Russia?',
 {'answer':'a','option':'a.11\n b.13\n c.1\n d.10'}],
['What’s the national animal of Australia?',
 {'answer':'a','option':'a.Red Kangaroo\n b.Dingo\n c.Platypus\n d.Rainbow Lorikeet'}],
['Name the best-selling book series of the 21st century?',
 {'answer':'c','option':'a.Beloved\n b.The Great Gatsby\n c.Harry Potter\n d.Beloved'}],
['Name the longest river in the world?',
 {'answer':'a','option':' a.The Nile\n b.Amazon River\n c.Paraná River\n d.Irtysh River'}],
['How many stripes are there on the US flag?',
 {'answer':'c','option':'a.10\n b.12\n c.13\n d.20'}],
['What’s the national flower of Japan?',
 {'answer':'a','option':'a.Cherry blossom\n b.Peony\n c.Orchid\n d.Lily'}],
]
#Name 
print ("Welcom to the Quiz")
while True:     
    name = input("what is your name : ")
    if name.isalpha():        
        break
    print("q.py  characters A-Z onle")
#Rules
rule = input("Please enter y if you wamt to read the rules\nor any other key if you want to exit:")

if rule ==  'N' or rule  ==  'n' or  rule == 'No' or rule == 'no': 
    print("see you next time")
    exit()

else:
    print("You will be geven a qushten and multboul ansers\nand you have to chowes the right anser : ")

#Ask if they are ready to take the quiz
status = input("Are you ready to take the quiz :{}?: \na. Yes \nb. No \n=>".format( name))

#What if the user is not ready
if status == 'No' or status == 'no' or status == 'n' or status == 'N' : 
    print("See you next time.")
    exit()
    
#what if the user is ready
else:
    print("Welcome to the quiz.")

    
index = 0
score = 0
optnum = 0
while len(gkquiz)>0:
   data = gkquiz[0]
   q = data[0]
   data = data[1]
   answer = data['answer']
   option = data['option']
 
   print(q)
   print(option)
 
   while True:
     user_answer = input("Plaes inter you anser her : ").lower()
     if user_answer == 'a' or user_answer == 'b' or user_answer == 'c' or user_answer == 'd':
         if user_answer == answer:
             print("Good work")
             score += 1
             print("Your scoer is",score)
         else:
             print("The answer is  wrong the right answer is",answer)
             print("Your scoer is",score)
         del gkquiz[0]
         break
     else:
         print("Enter your answer in a,b,c,d")
