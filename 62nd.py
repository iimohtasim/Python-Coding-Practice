# Write a program to print the factorial of number.
n = int(input("Enter the num: "))
fact = 1
for i in range(1,n):
    fact = fact*i
    i = i+1
print("",fact)