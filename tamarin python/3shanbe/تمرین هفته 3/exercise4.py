str='Salam Rooz Bekheir 222 @@&212'
isnum1=0
islower1=0
isupper1=0
isalpha1=0
sidentifier1=0
all=0
for c in str:
    all+=1
    if c.isdigit():
        isnum1+=1
    elif c.islower():
        islower1+=1
    elif c.isupper():
        isupper1+=1
    elif c.isalpha():
        isalpha1+=1
    elif c.isidentifier()== False:
        sidentifier1+=1


print("isnum1=",isnum1)
print("islower1=",islower1)
print("isupper1=",isupper1)
print("isalpha=",isalpha1)
print("sidentifier=",sidentifier1)
#print(str)
