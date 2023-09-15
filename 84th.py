'''A spam comment is defined as a text containsing following keywords
"make a lot of money","buy now","subscribe this","Click this".Write a program to detect these spams'''
# text = input("Enter the keywords: ")
# if text=="make a lot of money":
#     print("make a lot of money is spams")
# elif text=="buy now":
#     print("buy now is spams")
# elif text=="subscribe this":
#     print("subscribe this is spams")
# elif text=="click this":
#     print("click this is spam")
# else:
#     print("This is not spams")

text = input("Enter the keywords: ")
spam = True

if "make a lot of money" in text:
    spam = True
elif "buy now" in text:
    spam = True
elif "subscribe this" in text:
    spam = True
elif "click this" in text:
    spam = True
else:
    spam = False

if spam:
    print("This text is spam")
else:
    print("This text is not spam")