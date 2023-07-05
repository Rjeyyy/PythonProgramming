""" Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string."""


str1=str(input("Enter the first string:"))
str2=str(input("Enter the second string:"))
print(str1)
print(str2)
news1=str2[:2]+str1[2:]
news2=str1[:2]+str2[2:]

print("After swapping")
print(news1,news2)
