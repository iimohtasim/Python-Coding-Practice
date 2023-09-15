# A program to print the largest of three number:
num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
num3 = int(input("Enter the num3: "))
if num1>num2 and num1>num3:
    print("Num1 is greater than")
elif num2>num1 and num2>num3:
    print("Num2 is greater than")
else:
    print("Num3 is greater than")