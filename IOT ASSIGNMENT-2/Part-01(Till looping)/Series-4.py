def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    return fact
n=input("Enter a number: ")
a=sum([int(i) for i in n if i in('0','4','6')]) 
b=sum([int(i) for i in n if i in('5','7','9')]) 
print(sum([(-1)**i*a**j/factorial(j) for i,j in enumerate(range(1,b+1,2))]))  
