
sentence=input("please enter the number :").split(',')
for i in sentence:
    if((int(i,2))%5==0):
        print(int(i,2),end=",")