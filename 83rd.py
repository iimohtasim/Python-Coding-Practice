# Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume
# 3 subjects and take marks as an input from the user
math = int(input("Enter the marks of math: "))
phy = int(input("Enter the marks of physics: "))
chem = int(input("Enter the marks of chemistry: "))
total_marks = ((math+phy+chem)/300)*100
print(total_marks)
if total_marks>40 and phy>33 and math>33 and chem>33:
    print("Pass")
else:
    print("Fail")