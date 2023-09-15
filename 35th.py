'''The distance b/w  two cities(in kilometer) is input through the keyboard. Write a Program to convert and print this distance
in meters, feet, inches& centimeters. m= 1000, cm = 100000, inches = 39370.1, feet = 3280.84'''
km = int(input("Enter the kilometer between two cities: "))
m = km*1000
cm = km*100000
inches = km*39370.1
feet = km*3280.84
print("The meter is between two cities is ",m)
print("The centimeter is between two cities is ",cm)
print("The inches is between two cities is ",inches)
print("The feet is between two cities is ",feet)
