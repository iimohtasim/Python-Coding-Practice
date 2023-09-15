# The nonlocal Keyword
# def the_outer_function():
#     var=10
#     def the_inner_function():
#         nonlocal var
#         var = 14
#     print("The value inside the inner function",var)
#     the_inner_function()
#     print("The value inside the outer function",var)
#     the_outer_function()   # No result

# The pass Keyword
# def function_pass(argumets):
#     pass

# The return Keyword
# def func_with_return():
#     var=13
#     return var
# def func_with_no_return():
#     var=10
#     # return var
# print(func_with_return())
# print(func_with_no_return())

# The del keyword
# var1=var2=5
# del var1
# print(var2)
# print(var1)

# list_=['A','B','C']
# del list_[2]
# print(list_)

# text= 'hello user'
# print(text)
# text = 'hello\
#  user'
# print(text)

# The if Statement
# num=int(input("Enter the number: "))
# if num%2==0:
#     print("The given number is even number")

# The if_else statement
# a=22
# if a>9:
#     print("Greater")
# else:
#     print("Lesser")

# The elif statement
# num=int(input("Enter the number: "))
# if num ==10:
#     print("The given no is equal to 10")
# elif num == 50:
#     print("The given no is equal to 50")
# elif num == 100:
#     print("The given no is equal to 100")
# else:
#     print("The given no is not equal to 10,50,100")

# While loop
# i=0
# while i<5:
#     print("Harry")
#     i=i+1

# While loop with else
# counter = 0
# while counter<10:
#     counter = counter + 3
#     print("Python Loops")
# else:
#     print("Code block inside the else statement")

# The for loop
# numbers=[4,2,6,7,3,5,8,10,6,1,9,2]
# square =0
# squares=[]
# for values in numbers:
#     square = values**2
#     squares.append(square)
#     print("The list fo square is",squares)

# Using Else statement with for loop
# l = [1,7,8]
# for item in l:
#     print(item)
# else:
#     print("Done")

# Range function in Python
# for i in range(0,7):
#     print(i)

# The break Statement
# for i in range(0,80):
#     print(i)
#     if i == 3:
#         break

# The continue Statement
# for i in range(4):
#     # print(i)
#     if i==2:
#         continue
#     print(i)

# The Pass Statement
# l=[1,7,8]
# for item in l:
#     pass