# set
# s=set()
# s.add(1)
# s.add(2)
# print(s)

# using curly bracess
# days = {'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'}
# print(days)
# print(type(days))
# print("Display set in looping form")
# for i in days:
    # print(i)

# Using set() Method
# days = set(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
# print(days)
# print(type(days))
# print('Looping Through system')
# for i in days:
#     print(i)

# Adding items to the set
# Using add() method
# months = set(['January','February','March'])
# months.add("April")
# months.add("May")
# months.add("June")
# print("After add method in sets")
# print(months)
# for i in months:
#     print(i)

# # Using upadate function()
# months = set(['January','February','March'])
# months.update(['April','May','June'])
# print("After update function in set")
# print(months)
# for i in months:
#     print(i)

# Removing items from the set
# using discard() function
# months = set(['Jan','Feb','March','April','May','June'])
# months.discard('Jan')
# months.discard('June')
# months.discard('september')
# print("After the removing items from the sets")
# print(months)
# for i in months:
#     print(i)

# using remove function
# months = set(['Jan','Feb','March','April','May','June'])
# months.remove('Jan')
# months.remove('June')
# months.remove('agust')
# print("After the removing items from the sets")
# print(months)
# for i in months:
#     print(i)

# using pop() function
# months = set(['Jan','Feb','Mar','Apr','May'])
# print(months)
# months.pop()
# months.pop()
# print(months)

# using clear() function
# months = set(['Jan','Feb','Mar','Apr','May'])
# print(months)
# months.clear()
# print(months)

# union
# using union(/) operator
# month1 = {'Jan','Feb','Mar','Apr'}
# month2 = {'May','June','July'}
# print(month1/month2)  # unsupport union operator for set

# using union method
# month1 = set(['Jan','Feb','Mar','Apr'])
# month2 = set(['May','June','July'])
# print(month1.union(month2))

# The interaction of two sets
# using & operator
# month1 = set(['Jan','Feb','Mar','Apr'])
# month2 = set(['May','June','Jan'])
# print(month1 & month2)

# using interactin method
# month1 = {'Jan','Feb','Mar','Apr'}
# month2 = set(['May','June','Jan'])
# print(month1.intersection(month2))

# Difference of two sets
# using substraction(-) operator
# days1 = {'Mon','Tue','Wed','Thur'}
# days2 = {'Mon','Tue','Sun'}
# print(days1-days2)

# using difference method
# days1 = {'Mon','Tue','Wed','Thur'}
# days2 = {'Mon','Tue','Sun'}
# print(days1.difference(days2))

# Symmetric difference of two sets
# using ^ operator
# a={1,2,3,4,5,6}
# b={1,2,9,8,10}
# c = a^b
# print(c)

# using symmetric differenc of method
# a={1,2,3,4,5,6}
# b={1,2,9,8,10}
# print(a.symmetric_difference(b))

# Frozen Sets
# frozenset = frozenset([1,2,3,4,5])
# print(type(frozenset))
# print("\nPrinting the content of frozenset")
# for i in frozenset:
#     print(i)
# frozenset.add(6) # frozenset object has no attribut

# frozenset for the Dictionary
# dict = {"Name":"John","Country":"USA","ID":101}
# print(type(dict))
# frozenset= frozenset(dict)
# print(type(frozenset))
# for i in frozenset:
#     print(i)

# Python built in sets method
days = set([1,2,3,4,5,6])
# days2 = set([1,2,3,4,5,6])
# days2 = set([4,2,7,3,6,3,6,62,])
print(days)
# days.add(7)
# days.clear()
# days1 = days.copy()
# print(days1)
# days.difference_update(days2)
# days.discard(5)
# print(days.intersection(days2))
# print(days.intersection_update(days2))
# print(days.isdisjoint(days2))
# print(days.issubset(days2))
# print(days.issuperset(days2))
# days.pop()
# days.remove(6)
# print(days.symmetric_difference_update(days2))
# print(days.union(days2))
days.update('7')
print(days)