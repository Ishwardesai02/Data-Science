# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:35:40 2024

@author: ishwa
"""
Q1. Write a python program to print all even numbers from a 
given list of numbers in the same order and stop printing 
any after 237 in the sequence.
    
numbers= [     
386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 
328, 615, 953, 345,  
399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 
950, 626, 949, 687, 217,  
815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 
843, 831, 445, 742, 717, 958,743, 527] 
for i in numbers:
    if (i%2==0):
        if (i==237):
            break      
        print(i)

Q2. Write a python program to find a list of integers with 
exactly two occurrences of nineteen and at least three 
occurrences of five. Return True otherwise False. 
e.g. Input: 
[19, 19, 15, 5, 3, 5, 5, 2] 
Output: 
True 
Input: 
[19, 15, 15, 5, 3, 3, 5, 2] 
Output: 
False


l=[19, 19, 15, 5, 3, 5, 5, 2] 
def occurance(a):
    s=l.count(19)
    f=l.count(5)
    if (s==2 and f==3):
        return True
occurance(l)


Q3. Write a python program to find numbers that are greater 
than 10 and have odd first and last digits. 
e.g:  Input: 
[1, 3, 79, 10, 4, 1, 39, 62] 
Output: 
[79, 39] 
Input: 
[11, 31, 77, 93, 48, 1, 57] 
Output: 
[11, 31, 77, 93, 57] 


num=[11, 31, 77, 93, 48, 1, 57] 
def digit(l):
    for i in l:
        if i>10:   
            if (i%2!=0 and i%2!=0): 
                print(i)     
digit(num)
   

    
Q4. Write a python program to find the largest negative and
 smallest positive  numbers (or 0 if none). 
e.g. Input:   
[-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18] 
Output: 
[-6, 2] 


l=[-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]
for i in l:
    #s=min(l)
    if(min(l)>0):       
        print(l)



