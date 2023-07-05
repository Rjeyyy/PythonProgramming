"""Write a python program which reads your mail id, and extract the username from the mail id and generate the password such as username and the reverse of it."""


gmail=str(input("Enter the mail"))
print(gmail)
g=gmail.split("@")
user=g[0]
print(user)
p1=user[::-1]
p2=p1.upper()
pas=user+p2
print(pas)
