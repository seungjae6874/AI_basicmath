
import numpy as np
import math

a = np.ones(5)
print("1-a: ",a)
a = np.zeros(5)
print("1-b: ",a)
a = np.full(5,5)
print("1-c: ",a)
a = np.arange(1,6,1)
print("1-d: ",a)
a = np.arange(1,10,2)
print("1-e: ",a)
a = np.array([1,5,2,3,9])
print("1-f: ",a,"\n")

a = np.array([1,2,1,5,4])
b = np.arange(1,6,1)
print("\n2-a: ",a+b)
a = np.arange(1,6,1)
b = np.arange(5,0,-1)
print("2-b: ",a+b)
a = np.full(9,3,np.dtype(float))
b = np.full(9,1,np.dtype(float))
print("2-c: ",a-b)
a = np.arange(4,7,1)
b = np.arange(3,0,-1)
print("2-d: ",a-b)
a = np.full(4,1,dtype=np.float)
print("2-e: ",2*a)
a = np.array([0,4,2,3])
print("2-f: ",3*a)
a = np.arange(2,11,2)
print("2-g: ",0.5*a,"\n")

a = [1,2,3]
b = [9,8,7]

def DP(a,b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
print("\n3-a: ",DP(a,b))

a = np.arange(1,4,1)
b = np.arange(9,6,-1)
c0 = a[0]*b[0]
c1 = a[1]*b[1]
c2 = a[2]*b[2]
c = (c0,c1,c2)
print("3-b: ",np.sum(c),"\n")

c = np.array([6,2,4])
def vec_size(v):
    l = v[0]*v[0] + v[1]*v[1] + v[2]*v[2]
    return math.sqrt(l)
print("\n4: ",vec_size(c))

ax = np.array([1,0,0])
ay = np.array([0,1,0])
az = np.array([0,0,1])
bx = np.array([-2,1,4])
by = np.array([1,2,0])
bz = np.array([2,-1,1.25])
def DP5(a,b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2] #3-a에서 했지만 다른문제여서 다시 정의
print("\n\n5-a: %.2f %.2f %.2f %.2f"%(DP5(ax,ay),DP5(ax,az),DP5(ay,az),DP5(ax,ax)))
print("5-b: %.2f %.2f %.2f %.2f"%(DP5(bx,by),DP5(bx,bz),DP5(by,bz),DP5(bx,bx)))
v = np.arange(6,1,-2)
vx = DP5(v,bx)/DP5(bx,bx)
vy = DP5(v,by)/DP5(by,by)
vz = DP5(v,bz)/DP5(bz,bz)
v = np.array([vx,vy,vz])
print("5-c: [%.2f %.2f %.2f]"%(vx,vy,vz))
v = np.array([1,0,0])
vx = DP5(v,bx)/DP5(bx,bx)
vy = DP5(v,by)/DP5(by,by)
vz = DP5(v,bz)/DP5(bz,bz)
v = np.array([vx,vy,vz])
print("5-d: [%.2f %.2f %.2f]"%(vx,vy,vz))
v = np.full(3,2)
vx = DP5(v,bx)/DP5(bx,bx)
vy = DP5(v,by)/DP5(by,by)
vz = DP5(v,bz)/DP5(bz,bz)
v = np.array([vx,vy,vz])
print("5-e: [%.2f %.2f %.2f]"%(vx,vy,vz))
v = np.array(1*bx+2*by+3*bz)
vx = DP5(v,ax)/DP5(ax,ax)
vy = DP5(v,ay)/DP5(ay,ay)
vz = DP5(v,az)/DP5(az,az)
v = np.array([vx,vy,vz])
print("5-f: [%.2f %.2f %.2f]"%(vx,vy,vz))
v = np.array(4*bx+1*by+7*bz)
vx = DP5(v,ax)/DP5(ax,ax)
vy = DP5(v,ay)/DP5(ay,ay)
vz = DP5(v,az)/DP5(az,az)
v = np.array([vx,vy,vz])
print("5-g: [%.2f %.2f %.2f]"%(vx,vy,vz))
v = np.array(0*bx-1*by+2*bz)
vx = DP5(v,ax)/DP5(ax,ax)
vy = DP5(v,ay)/DP5(ay,ay)
vz = DP5(v,az)/DP5(az,az)
v = np.array([vx,vy,vz])
print("5-h: [%.2f %.2f %.2f]"%(vx,vy,vz))



