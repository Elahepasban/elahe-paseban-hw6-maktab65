total1=0
while True:
    money=input('input: ').split()
    if money[0] == 'w' or money[0] == 'W':
        total1 -= int(money[1])
    elif money[0] == 'D' or money[0] == 'd':
        total1 += int(money[1])
    elif money[0]=='-1':
        break
    else :
        pass
print( "Balance is : ",total1)















