# Strings
# name= "Mohtasim"
# print(name[0:5])
# print(name[4])
# print(name[1:3])

# slicing with skip value
# word = "amazing"
# print(word[1:6:2])
# print(word[0:7])
# print(word[0:])
# print(word[:7])

# Deleting the string
# baby = "amazing"
# del baby
# print(baby)

# The Format method
# using curly braces
# print("{} and {} both are best friend".format("Devansh","Abhishek"))
# Positional Argument
# print("{1} and {0}".format("Virat","Rohit"))
# keyword Arguement
# print("{a},{b},{c}".format(a="James",b="Peter",c="Rick"))

# Strings Function
baby = "amazing baby "
print(len(baby))
print(baby.endswith("ing"))
print(baby.count("a"))
print(baby.capitalize())
print(baby.find("baby"))
print(baby.replace('baby','darling'))
print(baby.casefold())
print(baby.isnumeric())
print(baby.swapcase())
print(baby.upper())
print(baby.title())
print(baby.isprintable())
print(baby.encode())