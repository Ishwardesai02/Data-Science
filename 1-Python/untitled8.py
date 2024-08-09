# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 08:47:39 2024

@author: ishwa
"""

----------------------"18/04/2024"--------------------------

#Array in Numpy
#Create ndarray
import numpy as np
arr=np.array([10,20,30])
print(arr)

#Create multidimentional array
arr=np.array([[10,20,30],[40,50,60]])
print(arr)

#use ndmin param to specify how many minimum dimensions you 
#wanted to create an array with minimum  dimension
arr=np.array([10,20,30,40],ndmin=3)
print(arr)

#change the datatype
# dtype parameter
arr=np.array([10,20,30],dtype=complex)
print(arr)

#Get dimension of array
arr=np.array([[10,20,30],[40,50,60],[15,26,37]],ndmin=3)
print(arr)
print(arr)

#Get datatype of array
arr=np.array([10,20,30])
print(arr.dtype)

#Get shape and size of array

arr=np.array([[10,20,30],[40,50,60]])
print(arr.size)   #Gives number of elements
print(arr.shape)

#Convert int to float
arr=np.array([[10,20,30],[40,50,60]],dtype="float")
print(arr)

#Create Sequence of integers using arrange()
#from 0 to 20 with step 3
arr=np.arange(0,20,3)
print(arr)

#Access single element using index
arr=np.arange(11)
print(arr)
print(arr[2])
print(arr[-2])

#Access elements of multidimensional array
arr=np.array([[10,20,30,90,80],[40,50,30,50,60]])
print(arr[1,2])
print(arr[0,0])
print(arr[-1,-3])
print(arr[1,-1])  

#Access array elements using slicing
arr=np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]
print(x)

x=arr[-1:-9:-2]
print(x)


#slicing of Multidimensional Array
arr=np.array([[10,20,30,90,80],[40,50,40,50,60],[10,20,70,90,30],[20,40,50,60,80]])
print(arr[1,2])
print(arr[1,:])
print(arr[:,1])

x=arr[:3,::2]
print(x)

#Integer Array Indexing
arr=np.arange(35).reshape(5,7)
print(arr)

#Boolean array Indexing 
#this advanced indexing occurs when an object is an array of


arr=np.arange(12).reshape(3,4)
print(arr)
rows=np.array([False,True,True])
rows
wanted_rows=arr[rows,:]
print(wanted_rows)

rows=np.array([True,False,True])
rows
wanted_rows=arr[rows,:]
print(wanted_rows)

#Numpy asarray()
list=[20,30,"i",40,50]
array=np.array(list)
print("Array :",array)
print(type(array))

#Numpy array Properties
#ndarray.shape
#ndarray.ndim
#ndarray.itemsize
#ndarray.size
#ndarray.dtype


#Shape
arr=np.array([[1,2,3],[4,5,6]])
arr
print(arr.shape)

#Resize the array
arr=np.array([[1,2,3],[4,5,6]])
arr.shape=(3,2)
print(arr)

#Reshape usage
arr=np.array([[1,2,3],[4,5,6]])
new_array=arr.reshape(3,2)
print(new_array)

#Apply Arthmatic Operation
arr1=np.arange(16).reshape(4,4)
arr2=np.array([1,3,2,4])
arr1

#add()
add_arr=np.add(arr1,arr2)
print(f"Adding two arrays :\n{add_arr}")

#Subtract
sub_arr=np.subtract(arr1,arr2)

print(f"Subtracting two arrays :\n{sub_arr}")

#Multiply
mul_arr=np.multiply(arr1,arr2)
print(mul_arr)
print(f"Subtracting two arrays :\n{mul_arr}")

#Division
div_arr=np.divide(arr1,arr2)
print(f"Subtracting two arrays :\n{div_arr}")

#To perform reciprocal operation
arr1=np.array([50,10.3,5,1,200])
rep_arr1=np.reciprocal(arr1)
print(f"After reciprocal function to array :\n{rep_arr1}")

#Numpy.power()

This Numpy power() function treats elements in the first input arr

#To perform power operation
arr1=np.array([3,10,5])
pow_arr1=np.power(arr1,3)
print(f"After applying power function to array :\n{pow_arr1}")

import numpy as np
arr1=np.array([3,10,5])
arr2=np.array([3,2,1])
pow_arr2=np.power(arr1,arr2)
print(pow_arr2)

#To perform mod function
#on numpy array
import numpy as np
arr1=np.array([7,20,13])
arr2=np.array([3,5,2])
arr1
arr1.dtype


#Create empty array
from numpy import empty
a=empty([3,3])
print(a)

#Create zero array
from numpy import zeros
a=zeros([3,3])
print(a)

#Create one array
from numpy import ones
a=ones([5])
print(a)

#Create array with vstack
from numpy import array
from numpy import vstack
#Create first array
a1=array([1,2,3])
print(a1)

#Create second Array
a2=array([4,5,6])
print(a2)

#vertical stack
a3=vstack((a1,a2))
print(a3)
print(a3.shape)

#Create hstack
from numpy import array
from numpy import hstack
#Create first array
a1=array([1,2,3])
print(a1)

#Create second Array
a2=array([4,5,6])
print(a2)

#vertical stack
a3=hstack((a1,a2))
print(a3)
print(a3.shape)


----------------------------------------------------------
-----------------------"23/04/2024"-----------------------
------------------------------------------------------------

# vector l1 norm
""" the l1 norm is calculated as the num of the absolute vector values,
where the absolute value of a scalar uses
the notation |a1|,
in effect the norm
is a calculation of the manhattan distance
from the origin of the vector space 
||v||1 = |a1|+|a2|+|a3|"""
from numpy import array
from numpy.linalg import norm # linag is linear algebra
#define vector
a=array([1,2,3])
print(a)
#calculate norm
l1=norm(a,1)
print(l1)


#vector l2 norm
""" the notation for the l2 norm of a vector
x is ||x||power of 2
to calulate the l2 norm of a vector,take the square root of the
sum of the squared vector values
another name for l2 norm of a vector is euclidean distance
this is often used for calculation the error in machine learnng models"""
from numpy import array
from numpy.linalg import norm # linag is linear algebra
#define vector
a=array([1,2,3])
print(a)
#claculating norm
l2=norm(a)
print(l2)

#triangular matrices
#used in image processing
from numpy import array
from numpy import tril # triangular lower matrix
from numpy import triu # triangular upper matrix
#define square matrix
M=array([
    [1,2,3],
    [1,2,3],
    [1,2,3]])
print(M)
#lower triangular matrix
lower=tril(M)
print(lower) # if we write only lower and not print(lower) then in output it will come comma
#upper traingular matrix
upper=triu(M)
print(upper)

#diagonal matrix
from numpy import array
from numpy import diag 
#define sqaure matrix
M=array([
    [4,2,3],
    [1,5,3,],
    [1,2,6]])
print(M)
#extract diagonal vector
d=diag(M)
print(d)
#create diagonal matrix from vector
d=diag(d)
print(d)

#identity matrix 
from numpy import identity
I=identity(3)
print(I)

#orthogonal matrix
"""the matrix is said to be an orthogonal matrix if the product
of a matrix and its transpose gives an identity value"""

from numpy import array
from numpy.linalg import inv
#define orthogonal matrix
Q=array([
    [1,0],
    [0,-1]])
print(Q)
#inverse equivalence
v=inv(Q)
print(Q.T)
print(v)
#identity equivalence
I=Q.dot(Q.T)
print(I)


----------------------------------------------------------
-----------------------"24/04/2024"-----------------------
-----------------------------------------------------------
#Define Matrix
A=array([[1,2],[3,4],[5,6]])
print(A)

#Calculate Transpose
C=A.T
print(C)

#Inverse Matrix
from numpy import array
from numpy.linalg import inv
A=array([[1,2],[3,4]])
print(A)
B=inv(A)
print(B)

#Multiply A and B
I=A.dot(B)
print(I)

#########################################
#Sparse matrix
from numpy import array
from scipy.sparse import csr_matrix
#Create Dense matrix

A=array([[1,0,0,1,0,0],[0,0,2,0,0,1],[0,0,0,2,0,0]])
print(A)

#Convert to sparse matrix (CSR method)
S=csr_matrix(A)
print(S)

#Reconstruct dense matrix
B=S.todense()
print(B)


