def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    return fact
num1=int(input("Enter number1: "))
num2=int(input("Enter number2: "))
print(1+sum([num1**i/factorial(i) for i in range(2,num2+1,2)])) 
