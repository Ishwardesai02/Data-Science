# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:48:45 2024

@author: ishwa
"""

----------------------------------------------------------
-----------------------"24/04/2024"-----------------------
-----------------------------------------------------------

import matplotlib.pyplot as plt
X=range(1,50)
Y=[value * 3 for value in X]
print("Value of x :")
print(*range(1,50))

'''this is equivalent to 
i in range (1,50)
         print(i,end='')  '''

print("values of Y (thrice of x):")
print(Y)

#plot lines and /or markers of the axes
plt.plot(X,Y)

#Set the X axis label of the current axis
plt.xlabel('x-axis')
        
#Set the Y axis label of the current axis
plt.xlabel('Y-axis')
        
#set a title
plt.title('Sample Graph !')

#Display a figure

plt.show()

#############################################################
#Write  program to plot two or more lines
#on same plot with suitable legends of each line
import matplotlib.pyplot as plt
 #line 1 plot
x1=[10,20,30]
y1=[20,40,10]

#line 2 points
x2=[10,20,30]
y2=[40,10,30]

#plot lines and/or markers of the axes
plt.plot(x1,y1,label="line 1")
#plotting line 2 points
plt.plot(x1,y1,label="line 2")
#Set the X axis label of the current axis
plt.xlabel('x-axis')
        
#Set the Y axis label of the current axis
plt.ylabel('Y-axis')
        
#set a title
plt.title('Sample Graph !')
#Display the figure
plt.show()
#show a legend on the plot
plt.legend()

############################################3333
#Write  program to plot two or more lines
#on same plot with suitable legends of each line
import matplotlib.pyplot as plt
 #line 1 plot
x1=[10,20,30]
y1=[20,40,10]

#line 2 points
x2=[10,20,30]
y2=[40,10,30]

#plot lines and/or markers of the axes
plt.plot(x1,y1,color='blue',linewidth = 3,label = "line 1")
#plotting line 2 points
plt.plot(x1,y1,,color='red',linewidth = 3 ,label = "line 2")
#Set the X axis label of the current axis
plt.xlabel('x-axis')
        
#Set the Y axis label of the current axis
plt.ylabel('Y-axis')
        
#set a title
plt.title('Sample Graph !')
#Display the figure
plt.show()
#show a legend on the plot
plt.legend()


#######################################################
import matplotlib.pyplot as plt
 #line 1 plot
x1=[10,20,30]
y1=[20,40,10]

#line 2 points
x2=[10,20,30]
y2=[40,10,30]

#plot lines and/or markers of the axes
plt.plot(x1,y1,color='blue',linewidth = 3,label = "line1-dotted",linestyle='dotted')
#plotting line 2 points
plt.plot(x2,y2,color='red',linewidth = 3 ,label = "line2-dashed",linestyle='dashed')
#Set the X axis label of the current axis
plt.xlabel('x-axis')
        
#Set the Y axis label of the current axis
plt.ylabel('Y-axis')
        
#set a title
plt.title('Sample Graph !')
#show a legend on the plot
plt.legend()
plt.show()


---------------------------------------------------------
--------------------"25/04/2024"-------------------------
---------------------------------------------------------


#WAP to plot two or more lines
# and set the line markers

import matplotlib.pyplot as plt
# x axis values
x=[1,4,5,6,7]
#y axis values
y=[2,6,3,6,3]

#plotting the points
plt.plot(x,y,color='red',linestyle='dashdot',linewidth=3,
         marker='o',markerfacecolor='blue',markersize=12)

#Set the y limits of the current axes
plt.ylim(1,8)
#Set the xlimits of the currenty axes
plt.xlim(1,8)

#Naming the x axes
plt.xlabel('x-axis')
#Naming the y -axis
plt.plot('y-axis')

#Giving the title to my graph
plt.title('Display Marker')

#Function to show the plot
plt.show()

##########################################################33

#write python program to display
#a bar chart of the popularity of programming langauge

import matplotlib.pyplot as plt
x=['Java','Python','PHP','javascript','c++']
Popularity=[22.2,17.6,8.8,7.7,6.7]
x_pos=[i for i, _ in enumerate(x)]
plt.bar(x_pos,Popularity,color='blue')
plt.xlabel("Langauges")
plt.ylabel("popularity")
plt.title("Popularity of Programming langauge\n" + "worldwide,oct 2017 compared to a year ago")
plt.xticks(x_pos,x)
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()


###############
#plot horizotally
import matplotlib.pyplot as plt
x=['Java','Python','PHP','javascript','c++']
Popularity=[22.2,17.6,8.8,7.7,6.7]
x_pos=[i for i, _ in enumerate(x)]
plt.barh(x_pos,Popularity,color='red')
plt.xlabel("Langauges")
plt.ylabel("popularity")
plt.title("Popularity of Programming langauge\n" + "worldwide,oct 2017 compared to a year ago")
plt.yticks(x_pos,x)
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='green')
plt.show()


#########
#use diffrent colors for diffrent graphs
import matplotlib.pyplot as plt
x=['Java','Python','PHP','javascript','c++']
Popularity=[22.2,17.6,8.8,7.7,6.7]
x_pos=[i for i, _ in enumerate(x)]

plt.bar(x_pos,Popularity,color=['red','black','green','blue','yellow','cyan'])
#plt.bar(x_pos,Popularity,color='red')
plt.xlabel("Langauges")
plt.ylabel("popularity")
plt.title("Popularity of Programming langauge\n" + "worldwide,oct 2017 compared to a year ago")
plt.xticks(x_pos,x)
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='green')
plt.show()

#############################
import matplotlib.pyplot as plt
blood_sugar=[113,85,150,149,88,93,115,135,80,77,82,129]
plt.hist(blood_sugar,rwidth=0.8)
plt.hist(blood_sugar,rwidth=0.5,bins=4)

plt.xlabel("Sugar levels")
plt.ylabel("Number of Patients")
plt.title("Number of patients")

plt.hist(blood_sugar,bins=[80,100,125,150],rwidth=0.8,color='green')

############################################################
#Box plot
#import libraries
import matplotlib.pyplot as plt
import numpy as np

#craeting dataset ]
np.random.seed(10)
data=np.random.normal(100,20,200)

fig=plt.figure(figsize=(10,7))

#creating plot
plt.boxplot(data)
plt.show

#######################################################
import matplotlib.pyplot as plt
import numpy as np

#craeting dataset ]
np.random.seed(10)
data_1=np.random.normal(100,10,200)
data_2=np.random.normal(90,20,200)
data_3=np.random.normal(80,30,200)
data_4=np.random.normal(70,40,200)

data=[data_1,data_2,data_3,data_4]
fig=plt.figure(figsize=(10,7))

#Creating axes instance
ax=fig.add_axes([0,0,1,1])
#creating plot
bp=ax.boxplot(data)