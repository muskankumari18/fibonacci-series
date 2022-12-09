def f(n):
    a=0
    b=1
    if n<0:
        print("Invalid number")
    elif n==0:
        print(n," is a fibonacci number")
        
    elif n==1:
        print(n," is a fibonacci number")
    else:
        for i in range(1,n+1):
            c=a+b
            a=b
            b=c
            if c==n:
                print(n," is a fibonacci number")
                break
            elif c>n:
                print(n," is not a fibonacci number")
                break
           
n=int(input("Enter how many values you want to check: "))
for i in range(1,n+1):
    a=int(input("Enter value: "))
    f(a)
