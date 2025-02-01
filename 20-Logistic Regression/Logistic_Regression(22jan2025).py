# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:10:28 2025

@author: Vaishnavi
"""
#OLS method
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import roc_curve,auc
from sklearn.metrics import classification_report
claimants=pd.read_csv("C:/Users/ADMIN/20-Logistic Regression/claimants.csv")
#the 0th column is CASENUM which is not useful,hence drop the column
c1=claimants.drop("CASENUM",axis=1)
c1.head()
c1.describe()
#let us check the null values
c1.isna().sum()
#There are several null values around 200
###
#let us use mean imputation for continuous data and mode imputation
#for discrete data
mean_value=c1.CLMAGE.mean()
mean_value
c1.CLMAGE=c1.CLMAGE.fillna(mean_value)
c1.CLMAGE.isna().sum()
###
#for descrete value like CLMSEX we need to use the mode imputation
mode_CLMSEX=c1.CLMSEX.mode()
mode_CLMSEX
#Here if you will observe the output it is 0 1 i.e
#mode_CLMSEX[0]=0,mode_CLMSEX[1]=1,we are passing mode_CLMSEX[0]
c1.CLMSEX=c1.CLMSEX.fillna((mode_CLMSEX)[0])
c1.CLMSEX.isna().sum()
#CLMINSUR
mode_INSUR=c1['CLMINSUR'].mode()
mode_INSUR
c1.CLMINSUR=c1.CLMINSUR.fillna((mode_CLMSEX)[0])
c1.CLMINSUR.isna().sum()
#SEATBELT
mode_SB=c1['SEATBELT'].mode()
mode_SB
c1.SEATBELT=c1.SEATBELT.fillna((mode_SB)[0])
c1.SEATBELT.isna().sum()
#####
#MOdel Building 
logit_model=sm.logit("ATTORNEY~CLMAGE+LOSS+CLMINSUR+CLMSEX+SEATBELT",data=c1).fit()
logit_model.summary()
logit_model.summary()
#LEt us go for predictionm
pred=logit_model.predict(c1.iloc[:,1:])
#################
#to derive the ROC curve
#ROC curve has tpr on y axis and for on x axis ,ideally tp must be hugh and fpr must be low
fpr,tpr,thresholds=roc_curve(c1.ATTORNEY,pred)
#TO identify optimum threshold
optimal_idx=np.argmax(tpr-fpr)
optimal_threshold=thresholds[optimal_idx]
optimal_threshold
#0.529 , by default you can take 0.5 value as threshiold 
#Now we want to identify if new va;ue is given to the model , it will
#fall in which region 0 or 1 for that we need to derive ROC curve 
#TO draw ROC curve
import pylab as pl
i=np.arange(len(tpr))
roc=pd.DataFrame({
    'fpr':pd.Series(fpr,index=i),
    'tpr':pd.Series(tpr,index=i),
    '1-fpr':pd.Series(1-fpr,index=i),
    'tf':pd.Series(tpr-(1-fpr),index=i),
    'thresholds':pd.Series(thresholds,index=i)
    })

#THis code creates a dataframe called roc using pandas(pd)
#it oraganizes various metrics related to the Recevier Operating Characteristics 
#Into coljumn .each column represents a specific metric , and the rows are index
#Plot ROC curve
plt.plot(fpr,tpr)
plt.xlabel("False positive rate");plt.ylabel("True Positive rate")
roc_auc=auc(fpr,tpr)
print("Area under the curve %f"%roc_auc)

##
##let us add prediction column in dataframe 
c1["pred"]=np.zeros(1340)
c1.loc[pred>optimal_threshold,"pred"]=1
#IF predicted value is greater than thereshold the change pred colunmn to 1
##Classification report

classification=classification_report(c1["pred"],c1["ATTORNEY"])
classification
###Spliting the data into train test data
train_data,test_data=train_test_split(c1,test_size=0.3)
#model building usingf
model=sm.logit("ATTORNEY~CLMAGE+LOSS+CLMINSUR+CLMSEX+SEATBELT",data=train_data)
model.summary()
model.summary2()

#AICis 1157
#prediction on test dxata
test_pred=model.predict(test_data)
test_data["test_pred"]=np.zeros(402)

#taking threshold value as optimal threshold value
test_data.loc[test_pred>optimal_threshold,"test_pred"]=1
#Confusion matrix
#Confusion matrix
confusion_matrix=pd.crosstab(test_data.test_pred,test_data.ATTORNEY)
confusion_matrix

accuracy=(131+151)/(131+151+62+58)
#Denotes (tp+tn)/(tp+tn+fp+fn)
#Equivalent to accuracy=(confusion_matrix.iloc[0,0]+confusion_matrix.iloc[1,1])/(confusion_matrix.iloc[0,0]+confusion_matrix.iloc[0,1]+confusion_matrix.iloc[1,0]+confusion_matrix.iloc[1,1])
accuracy
##

classification_report