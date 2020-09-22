# rishabh-rawat
a=0
b=1
n=int(input("enter the value of n: "))
sum=0
while n>0:
    print(sum,end=" ")
    n-=1
    a=b
    b=sum
    sum=a+b
