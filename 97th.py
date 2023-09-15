# Write a program to find whether a given number is prime or not
num = int(input("Enteer the number: "))
if num%num==0 and num%1==0 and num%2!=0:
    print("Prime No")
else:
    print("Not Prime no")