# Write a program to determine whether a character entered by the user is lower case or not (a-z = 97 - 122):
char = int(input("Enter the char: "))
# lower = (char >= 97) and (char >= 122)
# print("lower case",lower)
if (char >= 97) and (char <= 122):
    print("Character is lower case ")
else:
    print("Character is not lower case")