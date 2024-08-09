# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 09:05:47 2024

@author: ishwa
"""

1. Write a Pandas program to convert Series of lists to one Series. 
Sample Output:  
Original Series of list 
0    [Red, Green, White] 
1          
 [Red, Black] 
2              
 [Yellow] 
dtype: object 
One Series 
0       
Red 
1     Green 
2     White 
3       
Red 
4     Black 
5    Yellow 
dtype: object 

import pandas as pd

s=pd.Series(['Red', 'Green', 'White','Red', 'Black','Yellow'])
df1=pd.Series(['Red', 'Green', 'White'])
df2=pd.Series(['Red', 'Black']),
df3=pd.Series (['Yellow'])

df=pd.concat([df1,df2,df3])
print(df)

2. Write a python NLTK program to split the text sentence/paragraph into 
a list of words. 


import nltk
from nltk import word_tokenize
text = ''' 
Joe waited for the train. The train was late.  
Mary and Samantha took the bus.  
I looked for Mary and Samantha at the bus station. 
''' 
s1=text.split()
#s=word_tokenize(text)
print(s1)


3. Create a result array by adding the following two 
NumPy arrays. Next, modify the result array by 
calculating the square of each element 

import numpy as np
arrayOne = np.array([[5, 6, 9], [21 ,18, 27]]) 
arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]]) 
s=(arrayOne+arrayTwo)
print(s)
sq=pow(s,2)
print(sq)

4. Write a python program to extract word mention someone in
 tweets 
using @ from the specified column of a given DataFrame. 
DataFrame: ({ 
'tweets': ['@Obama says goodbye','Retweets for @cash','A political
          endorsement in 
@Indonesia', '1 dog = many #retweets', 'Just a simple #egg'] 
})
          
import re
pattern="@[a-z]*\.[a-zA-Z0-9]"
print(DataFrame,pattern)
           

5. Write a NumPy program to compute the mean, standard 
deviation,and  variance of a given array along the second axis. 

import numpy as np
df=np.array([0 ,1 ,2, 3, 8, 5])
s=df.mean()
print(s)

var=df.var()
print(var)



sd=df.std()
sd





