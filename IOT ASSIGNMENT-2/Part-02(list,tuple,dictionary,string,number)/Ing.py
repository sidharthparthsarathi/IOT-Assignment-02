st=input("Enter a String: ")
if len(st)<3 : print(st)
elif not st.endswith('ing'): print(st+'ing')
else: print(st+'ly')
