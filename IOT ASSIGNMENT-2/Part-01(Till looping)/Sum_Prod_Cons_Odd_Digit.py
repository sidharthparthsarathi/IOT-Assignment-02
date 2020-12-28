num=list(filter(lambda x : int (x)%2!=0,input("Enter a number: ")))
print(sum(int (num[i]) * int (num[i + 1 ]) for i in range(0,len(num)-1))) 
