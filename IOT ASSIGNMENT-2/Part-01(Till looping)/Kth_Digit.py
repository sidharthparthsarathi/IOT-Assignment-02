n = input ( " Enter a number: " )
k = int ( input ( " Enter K: " ))
print("\n Front: ",n[k - 1 ]," \n Back: ",n[-k]) if k<len(n) else print(" \n Invalid K " ) 
