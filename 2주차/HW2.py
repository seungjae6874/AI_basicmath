#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1번 문제


# In[214]:


import numpy as np
a = np.array([[2,5,1],[8,0,4],[6,2,9]])
b = np.array([[3,5,1],[0,9,4],[12,8,6]])
print("1-a: ",np.shape(a))
print("1-b: ",np.sum(a,axis=0))#행들의 합이니까 1열에대한 행의합은 16이맞다
print("1-c: ",np.sum(a,axis=1))
print("1-d: ",a[0,:],a[1,:],a[2,:])
print("1-e: ",a[:,0],a[:,1],a[:,2])
print("1-f:\n",np.matmul(a,b))
print("1-g:\n",a*b)


# In[30]:


#2번문제


# In[215]:


a = np.array([[2,5,1],[8,0,4],[6,2,9]])
x = np.array([1,2,3]).reshape(3,1)
print("2-a:\n",a*2)
c = np.array(a[:,0])
d = np.array(2*a[:,1])
e = np.array(3*a[:,2])
f = np.array([c,d,e])
print("2-b:\n",np.transpose(f))
r1 = a[0,:]
r2 = a[1,:]
r3 = a[2,:]
rsum = np.array([r1,2*r2,3*r3])


# In[216]:


a = np.array([[2,5,1],[8,0,4],[6,2,9]]).reshape(3,3)
x = np.array([1,2,3]).reshape(3,1)
def trans(A,y):
    z = np.zeros([np.shape(A)[1],np.shape(y)[1]],int)
    l = np.shape(y)[0]
    for i in range(l):
        z[i,:] = np.dot(A[i,:],y)
    return(z.reshape(1,3))
        
print("2-d:\n",trans(a,x))
print("2-e:\n",np.dot(a,x).reshape(1,3))


# In[217]:


#3번


# In[218]:


a = np.array([[6,7,3],[0,1,5],[6,2,1]],int)
b = np.array([[2,2,1],[8,3,4],[9,12,9]],int)
print("3-a:\n",a*b)


# In[219]:


def trans_comb(A,B):
    #B*A
    l1 = np.shape(A)[1]
    l2 = np.shape(B)[0]
    z = np.zeros([l1,l2],int)
    for i in range(l1):
        for j in range(l2):
            z[i,j] = np.dot(A[i,:],B[:,j])
    return(z)
print("3-b:\n",trans_comb(a,b))
print("3-c:\n",np.dot(a,b))


# In[220]:


#4번


# In[235]:


a = np.array([[1,3],[4,15]],int)
b = np.array([[1,3],[4,12]],int)
def determinant(A):#2*2 matrix
    sum = A[0,0]*A[1,1]-A[0,1]*A[1,0]
    return sum
print("4-a:\n",determinant(a),determinant(b))
print("4-b:\n",round(np.linalg.det(a),2),round(np.linalg.det(b),2))


# In[236]:


#5번


# In[239]:


a = np.array([[1,1,3],[1,2,4],[1,1,2]],int)
print("5-a:\n",np.linalg.inv(a))
b = np.linalg.inv(a)
print("5-b:\n",np.matmul(a,b))


# In[ ]:




