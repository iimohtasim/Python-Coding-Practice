name = input("Enter the name: ")
date = input("Enter the date: ")
letter = '''Dear <|Name|>
    You are selceted
    <|Date|>'''
letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)

