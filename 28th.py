# Write a Program to convert number of days  into months and days(Hint: 45 days- 1 months 15 days)
num = int(input("Enter the num: "))
months = num%30
days = num/30
print(int(months))
print(int(days))        # May be right output
