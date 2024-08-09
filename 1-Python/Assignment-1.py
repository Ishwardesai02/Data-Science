# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 23:11:26 2024

@author: ishwa
"""
------------------------------------------------------------------------
Q1:Mailing Address
'''Write a program that displays your name and complete mailing address 
formatted in the manner that you would usually see it on the outside of 
an envelope. Your program does not need to read any input from the user.'''

Name="Ishwar Desai"
Address="At/post Astagaon tal. Rahata dist. Ahmednagar"
pin=423107
print(f"Name is {Name} and Address is {Address} {pin}")
------------------------------------------------------------------------
Q2:Area of Room
'''Write a program that asks the user to enter the width and 
length of a room. Once the values have been read,
your program should compute and display the area of the room. 
The length and the width will be entered as floating point numbers.
Include units in your prompt and output message;either feet or meters, 
depending on which unit you are more comfortable working with.'''

def Area_r():
    print("Enter the Width and Length of room in meter")
    w=float(input("Enter width of room :"))
    l=float(input("Enter length of room :"))
    print("Area of Room is :", w*l)
Area_r()

-----------------------------------------------------------------------
Q3.Area of field

'''Create a program that reads the length and width of a farmer’s
 field from the user in feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.'''

def Feild_Area():
    l=int(input("Enter Length of the field : "))
    w=int(input("Enter width of the Field : "))
    area=l*w
    acre=area/43560
    print("Area of of the field in acre is : ",acre)
Feild_Area()

-----------------------------------------------------------------------
Q4:Bottle Deposites
'''
In many jurisdictions a small deposit is added to drink containers to 
encourage people to recycle them. In one particular jurisdiction, 
drink containers holding one liter or less have a $0.10 deposit, 
and drink containers holding more than one liter have a
$0.25 deposit. Write a program that reads the number of containers of 
each size from the user. Your program should continue by computing and 
displaying the refund that will be received for returning those
 containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.'''

def Container():
    C=int(input("Enter Number of Bottles :"))
    x=float(input("Enter the capacity of container :"))
    if(x<=1):
        print("Refund = $",C*0.10)
    else:
        print("Refund = $",C*0.25)
Container()

-----------------------------------------------------------------------
Q5:Tax and Tip 
'''
The program that you create for this exercise will begin by reading the
 cost  of a meal ordered at a restaurant from the user. 
Then your program will compute the tax and tip for the meal.
Use your local tax rate when computing the amount of tax owing. 
Compute the tip as 18 percent of the meal amount (without the tax). 
The output from your program should include the tax amount, the tip
amount, and the grand total for the meal including both the tax and
the tip. Format the output so that all of the valuesare displayed using
 two decimal places.'''
 
def restaurant():
    cost=int(input("Enter the cost of meal :"))
    tax=0.20*cost
    tip=0.18*cost
    total=tax+tip+cost
    print("Tax on meal is :",tax)
    print("Tip for meal :",tip)
    print("Total amount payable :",total)
restaurant()
    
-----------------------------------------------------------------------
Q6.Height Units
'''
Many people think about their height in feet and inches, even in some
countries that primarily use the metric system. 
Write a program that reads a number of feet from the user, 
followed by a number of inches. Once these values are read,
your program should compute and display the equivalent number of
 centimeters.'''
 
def Height():
    h=float(input("Enter Height in feets :"))
    print("Height is Centimeter ",h*30.48)
    H=float(input("Enter Height in inches :"))
    print("Height in centimeters :",H*2.54)
Height()
  
    
    


    



