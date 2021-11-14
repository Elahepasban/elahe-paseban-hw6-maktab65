
a=int(input("Enter number: "))

c=[]
for i in range(a):
    x=input("Enter name: ")
    c.append(x)
b=set(c)

d={}
for j in b:
    y=c.count(j)
    d[j]=y
s=sorted(d.items(), key=lambda x:x[1], reverse=True)

t=3
if len(b) < 3:
    t=len(b)
for k in range(t):
    print(s[k][0],s[k][1])














