def amstrong_num(n):
    p=int(n[0])
    q=int(n[1])
    r=int(n[2])
    s=int(n)
    if(s==(p**3)+(q**3)+(r**3)):
        print(s,"is an amstrong number")


       
x=int(input("enter a number between 100 to 1000"))
y=int(input("enter a number between 100 to 1000"))
for i in range(x+1,y):
    amstrong_num(i)
