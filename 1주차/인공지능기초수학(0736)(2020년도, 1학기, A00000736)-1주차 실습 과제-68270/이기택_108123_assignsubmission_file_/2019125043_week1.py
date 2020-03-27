import numpy as np
import math

def DP(a,b):
    index=0
    result=0
    for i in a:
        result = result+(i*b[index])
        index = index+1
        
    return result

def vec_size(v):
    return np.sqrt(sum(np.square(v)))

def coordinate(a,b,v):

    temp = np.dot(v,a)

    result = np.dot(temp,np.linalg.inv(b))

    return np.round(result,2)
        

a=np.ones(5)
print("1-a: ",a)


b=np.zeros(5)
print("1-b: ",b)

c=np.full(5,5)
print("1-c: ",c)

d=np.arange(1,6)
print("1-d: ",d)

e=np.arange(1,10,2)
print("1-e: ",e)

f=np.array([1,5,2,3,9])
print("1-f: ",f)

print("")

print("2-a: ",np.array([1,2,1,5,4])+d)

print("2-b: ",d + np.sort(d)[::-1])

print("2-c: ",np.full(9,3)-np.ones(9))

print("2-d: ",np.arange(4,7)-np.sort(np.arange(1,4))[::-1])

print("2-e: ",2*np.ones(4))

print("2-f: ",3*np.array([0,4,2,3]))

print("2-g: ",1/2*np.arange(2,11,2))

print("")

vectorA = [1,2,3];
vectorB = [9,8,7];

print("3-a: ",DP(vectorA,vectorB))

print("3-b: ",sum(np.array(vectorA)*np.array(vectorB)))

print("")

c=np.array([6,2,4])

print("4: ",vec_size(c))

print("")


# a coordinate

aX = np.array([1,0,0])
aY = np.array([0,1,0])
aZ = np.array([0,0,1])

cA = np.array((aX,aY,aZ))

# b coordinate

bX = np.array([-2,1,4])
bY = np.array([1,2,0])
bZ = np.array([2,-1,1.25])

cB = np.array((bX,bY,bZ))

aXY = sum(aX*aY)
aXZ = sum(aX*aZ)
aYZ = sum(aY*aZ)
aXX = sum(aX*aX)

bXY = sum(bX*bY)
bXZ = sum(bX*bZ)
bYZ = sum(bY*bZ)
bXX = sum(bX*bX)

print("5-a: ",aXY," ",aXZ," ",aYZ," ",aXX)
print("5-b: ",bXY," ",bXZ," ",bYZ," ",bXX)
print("5-c: ",coordinate(cA,cB,np.array([6,4,2])))
print("5-d: ",coordinate(cA,cB,np.array([1,0,0])))
print("5-e: ",coordinate(cA,cB,np.array([2,2,2])))
print("5-f: ",coordinate(cB,cA,np.array([1,2,3])))
print("5-g: ",coordinate(cB,cA,np.array([4,1,7])))
print("5-h: ",coordinate(cB,cA,np.array([0,-1,2])))



