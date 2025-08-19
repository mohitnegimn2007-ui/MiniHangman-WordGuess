import random
words=["Python","Pancake","Pankaj","Panda","Pyridine","Pants"]
a=random.randint(0,len(words))
computer=words[a]

for i in range(1,4):
    print("Attempt=",i)
    a=input("Enter your first letter:")
    if(a==computer[0]):
        print("correct")
        break
    elif(i==3):
        print("Out of attempts")
    else:
        print("incorrect")

for i in range(1,3):
    print("Attempt=",i)
    b=input("Enter your second letter:")
    if(b==computer[1]):
        print("correct")
        print("So your 2 letters are correct")
        print("Now you have to guess the correct word from",words)
        your=input("Enter your word:")

        if(your==computer):
            print("You guess it Correct.WoW")
            
        else:
            print("Oh!You failed")
            print(computer)
    
        break
    elif(i==3):
        print("out of attempts")
        print(computer)
        break

    else:
        print("incorrect")




    
    
    
    
    
    
    
    
    
