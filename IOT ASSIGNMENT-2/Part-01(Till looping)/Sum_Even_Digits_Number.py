def sumEven(number):
    sumEven=0
    while(number!=0):
        rem=number%10
        if((rem)%2==0):
            sumEven+=rem
        number//=10
    return sumEven
print("Enter a number to find the sum of it's even digits:",end=' ')
print(sumEven(int(input())))
