'''Write a program to great all the persons names stored in a list l1 and which starts with s
l1 = ["Harry","Soham","Sachin","Rahul"]'''

li=["Harry","Soham","Sachin","Rahul"]

for name in li:
    if name.startswith("S"):
        print("Hello " + name)