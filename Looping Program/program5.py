s=int(input())
e=int(input())
for i in range(s,e+1):
    if i==s:
        print()
        for j in range(1,11):
            print(i,"*",j,"=",i*j)
    else:
         print()
         for j in range(1,3):
             print(i,"*",j,"=",i*j)
