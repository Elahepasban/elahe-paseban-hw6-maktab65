def rhombus(n):
    for i in range(n+1):
       print(" "*(n-i), "* "*i)
    for j in range(n-1,0,-1):
       print(" " * (n - j), "* " * j)

def square(n):
    for i in range(n):
        print("* " * n)

def rectangle(n ,m):
    for i in range(n):
       print("* " * m)

def triangle(n):
    for i in range(n):
       print("* "*(i+1))

a=int(input("Enter Shape Type : \n 1)Square \n 2)Triangle \n 3)rhombus \n 4)rectangle \n"))
if a==1 :
    x=int(input("Enter width : "))
    print("Aria : " , x*x)
    square(x)
elif a== 2:
    x = int(input("Enter width : "))
    print("Aria : ", x * x/2)
    triangle(x)
elif a==3:
    x = int(input("Enter width : "))
    print("Aria : ", x * x *(3**(1/2))/2)
    rhombus(x)
elif a== 4:
    x = int(input("Enter width : "))
    y = int(input("Enter height : "))
    print("Aria : ", x * y)
    rectangle(x,y)
else :
    print("Invalid input")















