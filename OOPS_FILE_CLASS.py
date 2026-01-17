#!/usr/bin/env python
# coding: utf-8

# In[7]:


#CALCULATOR
class Calculator:
    def __init__(self,file):
        self.file=file
        self.a=0
        self.b=0
    def get(self):
        self.a=int(input("ENTER FIRST NUMBER"))
        self.b=int(input("ENTER SECOND NUMBER"))
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def save(self,operation,result):
        with open(self.file,"a") as f:
            f.write(f"{self.a} {operation} {self.b} = {result}")
    def read(self):
        with open(self.file,"r") as f:
            print(f.read())
c1=Calculator(r"E:\TEST\CALCI.txt")
while True:
    print("\n____MENU_____")
    print("0.  ENTER NUMBER")
    print("1.  ADD")
    print("2.  SUBTRACTION")
    print("3.  MULTIPLY")
    print("4.  READ FILE")
    print("5.  EXIT")
    choice=int(input("ENTER A CHOICE"))
    if choice==0:
        c1.get()
    elif choice==1:
        res=c1.add()
        print("SUM IS : ",res)
        c1.save("+",res)
    elif choice==2:
        res=c1.sub()
        print("DIFFERENCE IS : ",res)
        c1.save("-",res)
    elif choice==3:
        res=c1.mul()
        print("PRODUCT : ",res)
        c1.save("*",res)
    elif choice==4:
        c1.read()
    elif choice==5:
        print("EXITING.......")
        break
    else:
        print("INVALID CHOICE")


# In[9]:


#SIMPLE PROGRAM
class Student:
    def __init__(self,filename):
        self.filename=filename
    def add(self):
        name=input("NAME: ")
        marks=int(input("ENTER YOUR MARKS : "))
        with open(self.filename,"a") as f:
            f.write(f"{name} {marks}\n")
    def view(self):
        with open(self.filename,"r") as f:
            print(f.read())
s1=Student(r"E:\TEST\newtest.txt")
while True:
    print("_____MENU_____\n")
    print("1. ADD STUDENTS")
    print("2. VIEW STUDENTS")
    print("3.  EXIT")
    choice=int(input("ENTER CHOICE : "))
    if choice==1:
        s1.add()
    elif choice==2:
        s1.view()
    elif choice==3:
        print("EXITING......")
        break


# In[ ]:




