# Write a program to print the factorial of number.
fact = 1
n = int(input("Enter the no: "))
for i  in range(1,n):
    fact = fact * i
    i= i+1
print("",fact)