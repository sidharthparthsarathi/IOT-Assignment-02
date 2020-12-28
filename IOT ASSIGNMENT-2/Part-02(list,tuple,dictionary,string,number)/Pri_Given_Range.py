def prime_given_range(start, end):
    prime = [True for i in range(end+1)]
    pri=2
    while pri*pri <= end:
        if prime[pri]: 
            for i in range(pri*pri, end+1, pri): prime[i] = False
        pri+=1
    for i in range(max(2, start), end+1):
        if prime[i]: print(i, end=", ")
prime_given_range(int(input("Enter starting number: ")), int(input("Enter ending number: ")))
