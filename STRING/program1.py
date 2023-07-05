""" Write a Python program to get a string made of the first 2 and last 2 characters of a given string. 
If the string length is less than 2, return the empty string instead. """


string=str(input("Enter the string"))
st1=[]
if len(string)<2:
    print(st1)
else:
    print(string)
    print(string[0:2],string[-2:],sep="")   
