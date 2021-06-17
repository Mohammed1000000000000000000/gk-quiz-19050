#Asking ueser deteales


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

age()

                                                                               
