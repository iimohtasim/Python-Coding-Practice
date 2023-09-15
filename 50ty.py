'''A year is entered through the keyboard, Write a program to determine whether the year is leap or not. Use the logical  operator AND or OR '''
age = int(input("Enter the age: "))
# if age%100==0 and age%400==0:
#     print("leap year")
# else:
#     print("Not leap year")

if age%4==0:
    print("leap year")
else:
    print("Not leap year")