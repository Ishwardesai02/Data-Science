"""
Created on Fri Aug  9 08:27:44 2024

@author: ADMIN
"""
import pandas as pd
import numpy as np
univ1=pd.read_excel("D:/7-Clustring/University_Clustering.xlsx")
a=univ1.describe()
a
#we have one columnn state which is not really useful we will dropit
univ=univ1.drop(["State"],axis=1)
#we know that there is scale diffrence among the coloumns
#which we have to ren=move
#either by using normalization or standarization
#whwnever there is mixed data apply normalization
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#Now apply this noramalization function to univ dataframe
#for all the rows and column from1 until end
#since 0th column has university name hence skipped
df_norm=norm_func(univ.iloc[:,1:])
#you can chech the thr df_norm dataframe whioch is scaled
#between values of 0 to 1
#you can aply describe() function to new dataframe
b=df_norm.describe()
b
#before you apply clustering first you need to plot dendogram first
#now to create dendogram we need to measure the diatance
#we have to import linkage
import matplotlib.pylab as plt
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch
#linkage function gives us hirarchical or agglomerative clusteering 
#ref the help for linkage 
z=linkage(df_norm,method="complete",metric="euclidean")
plt.figure(figsize=(15,8))
plt.title("Hirarchical Clustring Dendogram")
plt.xlabel("Index")
plt.ylabel("Distance")

#dref help of dendogram 
#sch.dendograms(z)

sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()
#dendrogram
#applying agglomarative clustreing chossing 5 as clusteres from dendrogram
#whatever has been displayed in dengragram is not clusterring 
#it is just shoewing number of possible clusters

from sklearn.cluster import AgglomerativeClustering 
h_complete=AgglomerativeClustering(n_clusters=3,linkage="complete",metric="euclidean").fit(df_norm)
#apply labels to the clusters 
h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)
#Assign the series to univ datframe as column and name the coljumn 
univ['clust']=cluster_labels
#we want to replace the column 7 to 0 th position
univ1=univ.iloc[:,[7,1,2,3,4,5,6]]
#now check the univ 1 datframe
univ1.iloc[:,2:].groupby(univ1.clust).mean()
#from the output cluster 2 has got highest top10


