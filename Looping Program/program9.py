e=0
o=0
for i in range(1000):
    n=int(input("enter a num"))
    if(n==-1):
        break
    if n%2==0:
        e=e+1
    else:
        o=o+1
print("even num",e)
print("odd num",o)
