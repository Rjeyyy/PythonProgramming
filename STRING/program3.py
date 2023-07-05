#Write a Python function that takes a sentence and returns the longest word and the length of the longest one.


def long(l):
    m=l[0]
    leng=len(l[0])
    for i in l:
        if len(i)>leng:
             m=i
        return m
s=str(input("Enter the sentence"))
l=s.split()
ll=long(l)
print(s)
print(l)
print("Longest word is ", ll,"and its length is ",len(ll))
