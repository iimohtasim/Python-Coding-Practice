'''Calculate the area of circle and modify the same program to calculate the volume given its radius and height. 
Area of circle = pi*r*r / Volume of cirlce = pi *r*r*h'''

r = int(input("Enter the radius: "))
h = int(input("Enter the height: "))
A_circle = 3.14*r**2
V_circle = 3.14*r**2*h
print(A_circle)
print(V_circle)