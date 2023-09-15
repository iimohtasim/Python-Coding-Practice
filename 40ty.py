'''Write a program to find grade of a student given his marks based on below:
90-100 -> A
80-90  -> B
70-80  -> C
60-70  -> D
< 60   -> F
'''

marks = int(input("Enter the marks: "))
if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
elif marks>=60:
    print("D")
else:
    print("E")