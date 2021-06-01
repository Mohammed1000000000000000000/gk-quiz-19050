#Asking ueser deteales

print ("Welcom to the Quiz")

while True:
    name = input("what is your name : ")
    if name.isalpha():
        break
    print("please enter characters A-Z onle")
while True:
     Age = input ("What is yuor age : ")
     if Age.isnumeric():
         break

print ("Halow your Name is",name, "and yuor age is",Age)
