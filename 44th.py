'''Write a program to fnd out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass.
Assume 3 subjects and take marks as an input from the user'''
phy = int(input("Enter the  marks: "))
chem = int(input("Enter the marks: "))
math = int(input("Enter the marks: "))
t_marks = ((phy+chem+math)/300)*100
if t_marks<=40 and phy<=33 or chem<=33 or math<=33:
    print("Fail")
else:
    print("Pass")