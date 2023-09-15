'''If length of three side of a triangle are inuput through the keyboard. write a program to find the area of the triangle
area of triangle = s(s-a)(s-b)(s-c)|  sqrt = square root'''
import math
a = int(input("Enter the side a: "))
b = int(input("Enter the side b: "))
c = int(input("Enter the side c: "))
s = a+b+c/3                               # Answer is not happening
area = math.sqrt(s(s-a)(s-b)(s-c))
print("The are of triangle is: ",area)