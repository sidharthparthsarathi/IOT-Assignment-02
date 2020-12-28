def result(n):
    oddCount=0
    evenCount=0
    sumEven=0
    sumOdd=0
    while(n!=0):
        rem=n%10
        if(rem%2==0 and rem%4!=0):
            sumEven+=rem
            evenCount+=1
        if(rem%2!=0 and rem%3!=0):
            sumOdd+=rem
            oddCount+=1
        n//=10
    if(evenCount==0 and oddCount==0):
        return 0
    elif(evenCount==0):
        return sumOdd/oddCount
    elif(oddCount==0):
        return sumEven/evenCount
    return (sumEven/evenCount)-(sumOdd/oddCount)
print("Enter a number:",end=' ')
a=int(input())
print(result(a))
