# Write a program to find whether a year entered by the user is a leap year or not. Take year as input from the user.
year = int(input("Enter the year"))
if year%4==0:
    print("leap year")
else:
    print("Not leap year")