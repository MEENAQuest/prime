def check(n,flag):
    if n == 1:
        print("Not Prime")
    elif n > 1:
        for i in range(2,n):
            if n%i == 0:
                flag=True
                break
        if flag:
            print("Not Prime") 
        else:
            print("Prime")       

n=int(input("Enter a number: "))
flag=False
check(n,flag)    