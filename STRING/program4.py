""" Write a Python function which finds the length of the string, if the length of the string is multiple of 5, reverse the string and capitalize all the characters."""


def reverse(s):
    l=len(s)
    if l%5==0:
        t=s[::-1]
        u=t.upper()
    else:
         u=s  
    return u       

s=str(input("Enter the string"))
print(s)
print("New string is",reverse(s))
