import numpy as np
arr1=np.ones(5)
print("1-a : ", arr1)
arr2=np.zeros(5)
print("1-b : ",arr2)
arr3=np.full(5,5)
print("1-c : ",arr3)
arr4=np.arange(1,6)
print("1-d : ",arr4)
arr5=np.arange(1,10,2)
print("1-e : ",arr5)
arr6=np.array([1,5,2,3,9])
print("1-f : ",arr6)
print("\n")
ar1=np.array([1,2,1,5,4])
ar2=np.array([1,2,3,4,5])
print("2-a : ",ar1+ar2)
ar3=np.arange(1,6)
ar4=np.arange(5,0,-1)
print("2-b : ",ar3+ar4)
ar5=np.full(9,3)
ar6=np.ones(9)
print("2-c : ",ar5-ar6)
ar7=np.arange(4,7)
ar8=np.arange(3,0,-1)
print("2-d : ",ar7-ar8)
ar9=np.ones(4)
print("2-e : ",2*ar9)
ar10=np.array([0,4,2,3])
print("2-f : ",3*ar10)
ar11=np.array([2,4,6,8,10])
print("2-g : ",1/2*ar11)
print("\n")

tot=0
a=[0,0,0]
b=[0,0,0]

def DP(a,b):
    sum=0
    k=0
    a=[1,2,3]
    b=[9,8,7]
      
    for i in range(0,3):
        sum += a[i]*b[i]
    return sum

tot=DP(a,b)
print("3-a : ", tot)
a=np.array([1,2,3])
b=np.array([9,8,7])
c=a*b
tot= np.sum(c)
print("3-b : ",tot)
print("\n")

import numpy as np
c=np.array([6,2,4])
num=0
tot=0
def vec_size():
    vec=np.array([6,2,4])
    arr=np.array(vec)
    arr=np.array(arr)
    arr=np.square(arr)
    arr=np.sum(arr)
    arr=np.sqrt(arr)
    
    return arr

print("4 : ",vec_size())
print("\n")


a1=np.array([1,0,0])
a2=np.array([0,1,0])
a3=np.array([0,0,1])
b1=np.array([-2,1,4])
b2=np.array([1,2,0])
b3=np.array([2,-1,1.25])

tmp1=np.multiply(a1,a2)
tmp1=np.sum(tmp1)
tmp2=np.multiply(a1,a3)
tmp2=np.sum(tmp2)
tmp3=np.multiply(a2,a3)
tmp3=np.sum(tmp3)
tmp4=np.multiply(a1,a1)
tmp4=np.sum(tmp4)
print("5-a : ",tmp1,tmp2,tmp3,tmp4)

tmp1=np.multiply(b1,b2)
tmp1=np.sum(tmp1)
tmp2=np.multiply(b1,b3)
tmp2=np.sum(tmp2)
tmp3=np.multiply(b2,b3)
tmp3=np.sum(tmp3)
tmp4=np.multiply(b1,b1)
tmp4=np.sum(tmp4)
print("5-b : ",tmp1,tmp2,tmp3,tmp4)


cor1=np.array([6,4,2])
tmp5=np.multiply(cor1,b1)
tmp5=np.sum(tmp5)
tmp6=np.square(b1)
tmp6=np.sum(tmp6)
tmp5=tmp5/tmp6 
tmp7=np.multiply(cor1,b2)
tmp7=np.sum(tmp7)
tmp8=np.square(b2)
tmp8=np.sum(tmp8)
tmp7=tmp7/tmp8
tmp9=np.multiply(cor1,b3)
tmp9=np.sum(tmp9)
tmp10=np.square(b3)
tmp10=np.sum(tmp10)
tmp9=tmp9/tmp10
tot1=[tmp5,tmp7,tmp9]
print("5-c : ",tot1)

cor1=np.array([1,0,0])
tmp5=np.multiply(cor1,b1)
tmp5=np.sum(tmp5)
tmp6=np.square(b1)
tmp6=np.sum(tmp6)
tmp5=tmp5/tmp6
tmp5=round(tmp5,2)
tmp7=np.multiply(cor1,b2)
tmp7=np.sum(tmp7)
tmp8=np.square(b2)
tmp8=np.sum(tmp8)
tmp7=tmp7/tmp8
tmp7=round(tmp7,2)
tmp9=np.multiply(cor1,b3)
tmp9=np.sum(tmp9)
tmp10=np.square(b3)
tmp10=np.sum(tmp10)
tmp9=tmp9/tmp10
tmp9=round(tmp9,2)
tot1=[tmp5,tmp7,tmp9]
print("5-d : ",tot1)

cor1=np.array([2,2,2])
tmp5=np.multiply(cor1,b1)
tmp5=np.sum(tmp5)
tmp6=np.square(b1)
tmp6=np.sum(tmp6)
tmp5=tmp5/tmp6
tmp5=round(tmp5,2)
tmp7=np.multiply(cor1,b2)
tmp7=np.sum(tmp7)
tmp8=np.square(b2)
tmp8=np.sum(tmp8)
tmp7=tmp7/tmp8
tmp7=round(tmp7,2)
tmp9=np.multiply(cor1,b3)
tmp9=np.sum(tmp9)
tmp10=np.square(b3)
tmp10=np.sum(tmp10)
tmp9=tmp9/tmp10
tmp9=round(tmp9,2)
tot1=[tmp5,tmp7,tmp9]
print("5-e : ",tot1)

arr1=np.array([-2,1,2])
arr2=np.array([1,2,-1])
arr3=np.array([4,0,1.25])
mul=np.array([1,2,3])
x=np.multiply(mul,arr1)
x=np.sum(x)
y=np.multiply(mul,arr2)
y=np.sum(y)
z=np.multiply(mul,arr3)
z=np.sum(z)
tot=np.array([x,y,z])
print("5-f : ",tot)

arr1=np.array([-2,1,2])
arr2=np.array([1,2,-1])
arr3=np.array([4,0,1.25])
mul=np.array([4,1,7])
x=np.multiply(mul,arr1)
x=np.sum(x)
y=np.multiply(mul,arr2)
y=np.sum(y)
z=np.multiply(mul,arr3)
z=np.sum(z)
tot=np.array([x,y,z])
print("5-g : ",tot)

arr1=np.array([-2,1,2])
arr2=np.array([1,2,-1])
arr3=np.array([4,0,1.25])
mul=np.array([0,-1,2])
x=np.multiply(mul,arr1)
x=np.sum(x)
y=np.multiply(mul,arr2)
y=np.sum(y)
z=np.multiply(mul,arr3)
z=np.sum(z)
tot=np.array([x,y,z])
print("5-h : ",tot)
