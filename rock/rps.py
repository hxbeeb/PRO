import random
your_score=0
computer_score=0
#0-rock 1-paper 2-scissors
while True:
    a = input('enter r-rock p-paper s-scissors or q to quit-> ').lower()
    b = random.randint(0, 2)
    if a=='r':
        if b==2:
            print('scissors')
            print('you won')
            your_score+=1
        elif b==0:
            print('rock')
            print('draw')
        else:
            b==1
            print('paper')
            print('you lost')
            computer_score+=1
    elif a=='p':
        if b==0:
            print('rock')
            print('you won')
            your_score+=1
        elif b==1:
            print('paper')
            print("draw")
        else:
            b==2
            print('scissors')
            print('you lost')
            computer_score+=1
    elif a=='s':
        if b==1:
            print('paper')
            print('you won')
            your_score+=1
        elif b==0:
            print('rock')
            print("you lost")
            computer_score+=1
        else:
            b==2
            print("scissors")
            print('draw')
    elif a=='q':
        break
    else:
        continue
print("your score=",your_score)
print("computers score=",computer_score)
if your_score>computer_score:
    print("you defated the computer!!")
else:
    print('computer defeated you!')


