#Asking ueser deteales


print ("Welcom to the Quiz")

while True:
    name = input("what is your name : ")
    if name.replace(' ','').isalpha():
        break
    print("please enter characters A-Z onle")
while True:
    Age = input ("What is yuor age : ")
    if Age.replace(' ','').isnumeric():
        break
    print("please enter nambers onle") 


print("Hello",name,"your age is",Age,)

                                                                               
