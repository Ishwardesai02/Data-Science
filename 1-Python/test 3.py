# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:18:06 2024

@author: ishwa
"""

3.Write a Python program to reverse a string. 

S=input("Enter your string ")
r=S[::-1]
print(r)

4. Write a Python program to iterate over dictionaries using for loops. 

d={"Salary":20000,"Name":"Ram","Company":"meta"}
for k,v in d.items:
    print(k,":",v)


5. Using dict comprehension and a conditional argument create a dictionary from the current dictionary 
where only the key:value pairs with value above 2000 are taken to the new dictionary. 



6. Open the file data.txt using file operations. 

import pandas as pd
df=pd.read_csv("data.txt")
df

7. Define a array ,data = array([11, 22, 33, 44, 55]) find 0 th index 4 th index data 


import numpy as np
data = np.array([11, 22, 33, 44, 55])
a=data[0]
b=data[4]
print(a,b)


8. Write a Python program to filter a list of integers using Lambda.  
Original list of integers: 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
Even numbers from the said list: 
[2, 4, 6, 8, 10] 
Odd numbers from the said list: 
[1, 3, 5, 7, 9] 

l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
odd_lst=list(filter(lambda x:(x%2!=0),l))
print(odd_lst)

even_lst=list(filter(lambda x:(x%2==0),l))
print(even_lst)


9. Write a Pandas program to create the specified columns and rows from a given data frame. 

import pandas as pd
report={"name": ['Anna', 'Dinu', 'Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', 'venkat', 'Ajay', 'Dhanesh'], 
"score": [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan,8,19] ,
"attempts": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
"qualify": ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'] }

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df=pd.DataFrame(report,index=labels)
df

10. Define a array data = array([11, 22, 33, 44, 55]) and slice it from 1 to 4

import numpy as np
data = np.array([11, 22, 33, 44, 55])
arr=data[1:4]
print(arr)





