# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:22:25 2024

@author: ishwa
"""
------------------------------------------------------
Q1
'''1.Write a program that reads a letter of
 the alphabet from the user. If the user enters a, e,
 i, o or u then your program should display a 
 message indicating that the 
 entered letter is a vowel. If the user enters
 y then your program should display a message 
 indicating that sometimes y is a vowel, and 
 sometimes y is a consonant. Otherwise your program 
 should display a message indicating that the
letter is a consonant.'''

def Vowel():
    s=input("Enter the Alphabet :")
    if s=='a' or s=='A' or s=='E' or s=='e' or s=='I' or s=='i' or s=='o' or s=='O' or s=='u' or s=='U':
        print(s," is a Vowel")
    elif s=='Y' or s=='y':
        print("As you entered letter y, Sometimes it is a Vowel,and sometimes y is consonent ")
    else:
        print("Letter is a Consonant")
Vowel()

----------------------------------------------------
Q2.
'''Write a program that determines the name of a 
shape from its number of sides. Read the number of
 sides from the user and then report the appropriate
 name as part of a meaningful message. Your program
 should support shapes with anywhere from 3 up to 
 (and including) 10 sides. If a number of sides 
 outside of this range is entered then your program
 should display an appropriate error message.
 '''
 def sides():
     Sides=int(input("Enter the number of sides :"))
     shapes ={3: "triangle",
            4: "quadrilateral",
            5: "pentagon",
            6: "hexagon",
            7: "heptagon",
            8: "octagon",
            9: "nonagon",
            10: "decagon"}
     if 3<=Sides<=10:
         print("Shape is",shapes.get(Sides))
     else:
         print("Invalid side Entered")
 sides()

------------------------------------------------------------------
Q3.
'''The length of a month varies from 28 to 31 days.
 In this exercise you will create a program that reads
 the name of a month from the user as a string. 
 Then your program should display the number of days 
 in that month. Display “28 or 29 days” for February
 so that leap years are addressed'''

def months():
    Month=input("Enter name of the month :")
    days_in_month = {
        "January": 31,
        "February": "28 or 29",
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    
    
    day=days_in_month.get(Month)
    print(day)
months()
-------------------------------------------------------------------------------
Q4.
'''A triangle can be classified based on the lengths 
of its sides as equilateral, isosceles or scalene. 
All 3 sides of an equilateral triangle have the same 
length. An isosceles triangle has two sides that are 
the same length, and a third side that is a different
length. If all of the sides have different lengths
 then the triangle is scalene. Write a program that 
 reads the lengths of 3 sides of a triangle from the
 user. Display a message indicating the type of the
 triangle.
'''
def triangle():
    side1=int(input("Enter first side :"))
    side2=int(input("Enter second side :"))
    side3=int(input("Enter third side :"))
    if side1== side2==side3 :
        print("Triangle is Equilateral")
    elif side1==side2!=side3 or side1!=side2==side3 or side1==side3!=side2:
        print("Triangle is isoceles")
    elif side1!=side2!=side3:
        print("Triangle is scalene")
triangle()
    
-----------------------------------------------------
Q5.
'''The year is divided into three seasons: summer,
 rainy and winter. While the exact dates that the 
 seasons change vary a little bit from year to year
 because of the way that the calendar is constructed, 
 Write a program to display the season if date is 
 given.'''
 
def season():
    m=int(input("Enter the month :"))
    season_date={2:'Summer',3:'Summer',4:'Summer',5:'Summer'
                 ,6:'Mansoon',7:'Mansoon',8:'Mansoon',9:'Mansoon',
                 10:'Winter',11:'Winter',12:'Winter',1:'Winter'}
    s=season_date.get(m)
    print(s)
season()

    
    
    

    












        
