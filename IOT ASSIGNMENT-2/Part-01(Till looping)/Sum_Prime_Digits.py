def sumPrime(n):
    sumPri=0
    while(n!=0):
        rem=n%10
        if(rem==2 or rem==3 or rem==5 or rem==7):
            sumPri=sumPri+rem
        n=n//10
    return sumPri
print("Enter a number to find the sum of all prime digits:",end=' ')
print(sumPrime(int(input())))
