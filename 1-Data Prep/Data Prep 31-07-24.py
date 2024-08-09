# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 08:33:19 2024

@author: ishwa
"""

#Data pre Processing
import pandas as pd

df=pd.read_csv("C:/1-Data Prep/ethnic diversity.csv")
#let us check datatypes of column
df.dtypes
#salaries data type is float let us convert into int
df.Salaries=df.Salaries.astype(int)
df.dtypes
#now the datatype of salaries is int
#similarly age datatype must be float
#presently it is int
df.age=df.age.astype(float)
df.dtypes

----------------------------------

#identify the dupliactes
df_new=pd.read_csv("C:/1-Data Prep/education.csv")
duplicate=df_new.duplicated()
#output of this function is single column
#if there are duplicate records - TRUe
#if there are no duplicate records - False
#Series will be created
duplicate
sum(duplicate)
#output will be zero 
#now let us import another dataset
df_new1=pd.read_csv("C:/1-Data Prep/mtcars_dup.csv")
duplicate1=df_new1.duplicated()
duplicate1
sum(duplicate1)
#here are 3 duplicate records
#row 17 is duplicate of row 2 like wise you can 3 duplicate 
#records
#There is function called drop_duplicates()
#which will drop all the duplicate records

-----------------------------------------
#outliers traetment 
import pandas as pd
import numpy as np
import seaborn as sns
df=pd.read_csv("C:/1-Data Prep/ethnic diversity.csv")
#now let us find outliers in salaries
sns.boxplot(df.Salaries)
#There are outliers
#let us check outliers in age column
sns.boxplot(df.age)
#there are no outliers in age colukmn
#let us calculate outlier
IQR=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#have observed iqr in variable explorer
#no because iqr is in capital letters
#treated as constant
IQR
#if we will try as I,iqr or iqr then it will show
iqr=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
iqr
lower_limit=df.Salaries.quantile(0.25)-1.5*iqr
upper_limit=df.Salaries.quantile(0.75)+1.5*iqr
lower_limit,upper_limit
#############################################################
#Trimming
import numpy as np
import seaborn as sns
outliers_df=np.where(df.Salaries>upper_limit,True, np.where(df.Salaries<lower_limit,True,False))
outliers_df
#you can check the outliers of columns in variable explorer
df_trimmed=df.loc[~outliers_df]
df.shape
df_trimmed.shape
sns.boxplot(df_trimmed.Salaries)

import matplotlib.pyplot as plt
plt.violinplot(df_trimmed.Salaries)
plt.show()
###############################################################
#Replacement technique
import pandas as pd
df=pd.read_csv("C:/1-Data Prep/ethnic diversity.csv")
df.describe()
#record nummber 23has got outliers
#map all the outlier values to upper limit
df_replaced=pd.DataFrame(np.where(df.Salaries>upper_limit,upper_limit,np.where(df.Salaries<lower_limit,lower_limit,df.Salaries)))
#if the values are greater than the upper limit, then mapit to the upper limit
#and less than lower limit then map it to the lower limit
#if it is within the range then keep it as it is
sns.boxplot(df_replaced[0])
##############################################################################3
#winsorizer
from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['Salaries'])
#copy winsorizer and paste it in the top right help window to study it
df_t=winsor.fit_transform(df[['Salaries']])
sns.boxplot(df['Salaries'])
sns.boxplot(df_t['Salaries'])


################################################################

#zero variance and near zero variance
#If there is no variance in the feature
#trhen ML, will not get any intelligence ,so it is better to 
#have variance in the gfeature
import pandas as pd
df=pd.read_csv("C:/1-Data Prep/ethnic diversity.csv")
df.Salaries.var()
#here EMP ID in nominal data
#salary has 4.44444444444 which is not
#close to 0
df.var()==0
#none of them are equal to zero
df.var(axis=0)==0

#####################
#checking the null values
import pandas as pd
import numpy as np
df=pd.read_csv("C:/1-Data Prep/modified ethnic.csv")
#chevk nullvalues
df.isna().sum()


#create an imputer  that creates NAN values
#mean aur median used for numeric data
#mode is used for discreate data

from sklearn.impute import SimpleImputer
mean_imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
#check the dataframe
df['Salaries']=pd.DataFrame(mean_imputer.fit_transform(df[['Salaries']]))
df['Salaries'].isna().sum()


#median imputer
median_imputer=SimpleImputer(missing_values=np.nan,strategy='median')
#check the dataframe
df['age']=pd.DataFrame(mean_imputer.fit_transform(df[['age']]))
df['age'].isna().sum()

#mode imputer
mode_imputer=SimpleImputer(missing_values=np.nan,strategy='most_frequent')
#check the dataframe
df['Sex']=pd.DataFrame(mean_imputer.fit_transform(df[['Sex']]))
df['Sex'].isna().sum()


################################
import numpy as np
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE

#step1:
X,y=make_classification(n_samples=1000,n_features=20,n_informative=2,n_redundant=10,n_clusters_per_class=1,weights=[0.99],flip_y=0,random_state=1)
#show the original class distribution
'''
Parameters
n_sampels=1000:
        The total number of samples(datapoints) to generate.
        Here, 1000 sampples will be created
    
    n_features=20:
        The total number of features(columns) in the dataset
        Each sample will have 20 features
        
    n_informative=2:
        Number of informative features
        These features are udeful for prediictinf the target variables
        
    n_redundant=10:
        The number of redundant features
        These features are generated as random linear combinations
         
    n_clusters_per_class=1:
        The number of clusters per class
        Each class will have 1 cluster of points
        This parameter is useful for controlling the overlap between classes
    
    weights=[0.99]:
        the proportions of samples assigned to each class
        Here, 99% of samples will belong to one class
'''
print("Original class distribution:",np.bincount(y))

#step 2:apply SMOTE to balance the dataset
smote=SMOTE(random_state=42)
X_res,y_res=smote.fit_resample(X,y)

#show the new class distribution after applying 

print("Resampled class distribution:",np.bincount(y_res))


-------------------------------------------------------
--------------"05/07/2024"-----------------------------
-------------------------------------------------------

#show the origninal class distribution 

print(f"original class distribution :{np.bincount(y)}")

from sklearn.model_selection import train_test_split

#step 2:  split the data into trainning and testing sets

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

#step 3:apply SMOTE to balance the training dataset
smote=SMOTE(random_state=4)
X_train_res,y_train_res=smote.fit_resample(X_train,y_train)

#show the new class distribution after applying SMOTE
print(f"Resampled class distribution :{np.bincount(y_train_res)}")
 
from sklearn.ensemble import RandomForest 
#step4:train the classifier on the balanced dataset

clf=RandomForestClassifier(random_state=42)
clf.fit(X_train_res,y_train_res)



###############################################
#log tranformation technique

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#generate a sample dtaset
data=np.random.exponential(scale=2.0,size=1000)
df=pd.DataFrame(data,columns=['Value'])

#perform log transformation
df['LogValue']=np.log(df['Value'])

#plot the original and log transformation data

fig,axes=plt.subplots(1,2,figsize=(12,6))

#orginal data
axes[0].hist(df['Value'],bins=30,color='green',alpha=0.7)
axes[0].set_title('original Data')
axes[0].set_xlabel('Value')
axes[0].set_ylabel('frequency')

#log transformation data

axes[1].hist(df['LogValue'],bins=30,color='blue',alpha=0.7)
axes[1].set_title('Log Transformed Data')
axes[1].set_xlabel('log(Value)')
axes[1].set_ylabel('frequency')

plt.tight_layout()
plt.show()

