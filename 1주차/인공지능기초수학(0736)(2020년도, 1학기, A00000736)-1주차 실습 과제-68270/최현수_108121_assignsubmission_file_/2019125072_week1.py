#!/usr/bin/env python
# coding: utf-8

# In[75]:


import numpy as np
import math

a=np.ones(5)
print("1-a: ",a)

b=np.zeros(5)
print("1-b: ",b)

c=np.full((5),5)
print("1-c: ",c)

d=np.arange(1,6)
print("1-d: ",d)

e=np.arange(1,10,2)
print("1-e: ",e)

list1=[1,5,2,3,9]
f=np.array(list1)
print("1-f: ",f)

print()


# In[76]:


list1=[1,2,1,5,4]
list2=[1,2,3,4,5]
a=np.array(list1)
b=np.array(list2)
print("2-a: ",a+b)

a=np.arange(1,6)
b=np.arange(5,0,-1)
print("2-b: ",a+b)

a=np.full((9),3)
b=np.full((9),1)
print("2-c: ",a-b)

a=np.arange(4,7)
b=np.arange(3,0,-1)
print("2-d: ",a-b)

a=np.ones(4)
print("2-e: ",2*a)

list1=[0,4,2,3]
a=np.array(list1)
print("2-f:",3*a)

a=np.arange(2,11,2)
print("2-g: ",1/2*a)

print()


# In[73]:


def DP(a,b):
    c=a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
    return c

# a,b가 3개라고 문제에 미리 정의되어 있어 DP함수에 for문 사용 안 했습니다

a=[1,2,3]
b=[9,8,7]

print("3-a:",DP(a,b))

list1=[1,2,3]
list2=[9,8,7]
a=np.array(list1)
b=np.array(list2)

print("3-b:", np.sum(a*b))

print()


# In[82]:


def vec_size(vec):
    vec=vec**2
    return math.sqrt(sum(vec))

list1=[6,2,4]
c=np.array(list1)
print("4: ",vec_size(c))

print()


# In[126]:


list1=[1,0,0]
list2=[0,1,0]
list3=[0,0,1]
list4=[-2,1,4]
list5=[1,2,0]
list6=[2,-1,1.25]

ax=np.array(list1)
ay=np.array(list2)
az=np.array(list3)

bx=np.array(list4)
by=np.array(list5)
bz=np.array(list6)

print("5-a: ",np.sum(ax*ay),np.sum(ax*az),np.sum(az*ay),np.sum(ax*ax))
print("5-b: ",np.sum(bx*by),np.sum(bx*bz),np.sum(bz*by),np.sum(bx*bx))


#c~h문제 같은 하나의 함수를 이용해서 풀어보려고 했는데 역행렬을 구하는 것 까지 포함해 짜긴 힘들더라구요 ㅠㅠ..

# atob 함수(문제 c,d,e)는 강의에서 사용한 공식 이용해서 만들었습니다.
def atob(r,x,y,z):
    list=[sum(r*x)/sum(x**2),sum(r*y)/sum(y**2),sum(r*z)/sum(z**2)]
    c=np.array(list)
    return c
    
#btoa함수(문제 f,g,h)는 다른 선형대수학 강의 찾아보고 역행렬를 이용해 계산하는 방식으로 풀었습니다. 
# a coordinate의 역행렬 역시 단위벡터기에 따로 안넣었슴다
def btoa(r,x,y,z):
    
    #행렬식의 곱셈 이용하려면 bx,by,bz의 행과 열이 서로 바뀌어야 해서 b1,b2,b3 새로 만듦
    
    list1=[x[0],y[0],z[0]]
    b1=np.array(list1)
    
    list2=[x[1],y[1],z[1]]
    b2=np.array(list2)
    
    list3=[x[2],y[2],z[2]]
    b3=np.array(list3)

    list4=[sum(b1*r),sum(b2*r),sum(b3*r)]
    fin_b=np.array(list4)
    
    return fin_b

print("5-c: ",atob([6,4,2],bx,by,bz))
print("5-d: ",atob([1,0,0],bx,by,bz))
print("5-e: ",atob([2,2,2],bx,by,bz))

print("5-f: ",btoa([1,2,3],bx,by,bz))
print("5-g: ",btoa([4,1,7],bx,by,bz))
print("5-g: ",btoa([0,-1,2],bx,by,bz))

    

