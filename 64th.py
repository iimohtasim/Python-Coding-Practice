# Write a program to print the odd numbers from 1 to N natual number.
n=int(input("Enter the number: "))
sum=0
for i in range(1,n,2):
    print(i)
    sum = sum+i
print("Sum of odd number: ",sum)