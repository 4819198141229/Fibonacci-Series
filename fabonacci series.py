n=int(input("Enter the value of n:"))
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("The fabonacci series is: {} {}".format(a,b),end=" ")
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
