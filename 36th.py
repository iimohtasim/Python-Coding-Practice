'''If the marks obtained by a student in five different subjects are input through keyboard, Write a Program to find out the aggregrate
marks and percentage marks obtained by the student. Assume that the maximumm marks that can be obtained by a studnet in each subject is 100'''
s1_marks = int(input("Enter the subject1 marks: "))
s2_marks = int(input("Enter the subject2 marks: "))
s3_marks = int(input("Enter the subject3 marks: "))
s4_marks = int(input("Enter the subject4 marks: "))
s5_marks = int(input("Enter the subject5 marks: "))
agg = s1_marks+s2_marks+s3_marks+s4_marks+s5_marks
per = (agg/500)*100
print("The aggregrate 'marks of subjects is ",agg)
print("The percentage 'marks of subjects is ",per)
