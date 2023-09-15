'''Ramesh's basic salary is input through the keyboard. His dearness allowance is 40% of basic salary, and house rent allowance is 20% 
of basic salary. Write a Program t0 calculate his gross salary'''
bs = int(input("Enter the basic salary of ramesh: "))
allowance = (40/100) * bs
hr = (20/100)* bs
gross = bs + allowance + hr
print("The gross salary is ",int(gross))
