'''If cost price and selling price of an  item is input through keyboard, Write a Program to determine whether the seller has profit or 
incurred loss. Also determinne how much profit he made or loss he incurred.'''
cp = int(input("Enter the cost price: "))
sp = int(input("Enter the selling Price: "))
profit = sp-cp
loss = cp-sp
if sp>cp:
    print("Profit and he made of " + str(profit))
else:
    print("Loss and he made of" + str(loss))