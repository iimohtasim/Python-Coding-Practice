'''Write a Program to find the area & perimeter of rectangle & circle. Area of rectangle = l*b, Perimeter of circle = 2*pi*r
Pereimeter of rectngle = 2(l+b), Area_of_circle = pi*r**2*h'''
l = int(input("Enter the l: "))
b = int(input("Enter the b: "))
r = int(input("Enter the r: "))
h = int(input("Enter the h: "))

A_rectangle = l*b
P_rectangle = 2*(l+b)
A_circle = 3.14*r**2*h
P_circle = 2*3.14*r

print(A_rectangle)
print(P_rectangle)
print(A_circle)
print(P_circle)