num=int(input("Enter a number:"))
F=1
if num<0:
    print("Factorial not founf for negative numbers")
elif num==0:
    print("Factorial of zero is",F)
else:
    for i in range(1,num+1):
        print("Value of i is",i)
        F=F*i
    print("Factorial of",num,"is:",F)
