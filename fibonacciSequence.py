#Created by SHADOWMALICE
#Fibonacci Sequence

m1(input("What is the max number of your Fibonacci Sequence?"))
f1=1
f2=2
next = f1+f2
while f1 <= m1:
    print(f1)
    f1=f2
    f2=next
    next=f1+f2