print("Welcome to My Cyber Games!")

playing= input("Do you want to play? ")

if playing.lower() !="yes": 
    quit() 

print("Okay! Let's Get Started!","Best Of Luck.")
score=0    

answer= input("what does SUDO stand for? ").lower()
if answer.lower()=="It is convertar to Root":
    print('correct!')
    score+=1

else:
    print('incorrect!') 

answer= input("what does cd means? ").lower()
if answer.lower()=="It helps to enter the file":
    print('correct!')
    score+=1

else:
    print('incorrect!') 
answer= input("what does LS means? ").lower()
if answer.lower()=="It is  the list of a file":
    print('correct!')
    score+=1

else:
    print('incorrect!') 

print("You Got "+"str(score)"+"question correct!")
print("You Got"+"str((score/4)*100)+ %.")
