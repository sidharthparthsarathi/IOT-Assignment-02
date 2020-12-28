def sumOdd(number):
    sumOdd=0
    while(number!=0):
        if((number%10)%2==1):
            sumOdd+=number%10
        number//=10
    return sumOdd
print("Enter a number to find the sum of it's odd digits:",end=' ')
print(sumOdd(int(input())))
