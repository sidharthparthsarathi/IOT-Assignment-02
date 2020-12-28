st=input("Enter a String: ")
print(''.join([st[0]]+[c if c!=st[0] else '$' for c in st[1:]]))
