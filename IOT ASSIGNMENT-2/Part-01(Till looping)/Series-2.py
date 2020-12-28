def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    return fact
num1=int(input("Enter number1: "))
num2=int(input("Enter number2: "))
print(sum([(-1)**i*num1**j/factorial(j) for i,j in enumerate(range(1,num2+1,2))]))
