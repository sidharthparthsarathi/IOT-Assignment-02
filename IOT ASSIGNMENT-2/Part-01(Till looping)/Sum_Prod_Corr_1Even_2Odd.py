print(sum(i * j for (i,j) in zip(filter(lambda x : x%2==0,map(int,input("Enter first number: "))),filter(lambda x : x%2!=0,map(int,input("Enter second number: ")))))) 
