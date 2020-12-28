def sum(number):
    sumDigit=0
    while(number!=0):
        sumDigit+=number%10
        number//=10
    return sumDigit
print("Enter a number to find the sum of it's digits:",end=' ')
number=int(input())
print(sum(number))
