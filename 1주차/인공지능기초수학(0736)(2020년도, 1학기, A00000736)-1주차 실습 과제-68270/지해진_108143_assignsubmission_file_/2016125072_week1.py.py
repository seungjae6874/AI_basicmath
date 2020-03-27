import numpy as np

a1=np.ones(5)
print("1-a:",a1)

b=np.zeros(5)
print("1-b:",b)

c=np.full((5),5)
print("1-c:",c)

d=np.arange(1,6,1)
print("1-d:",d)

e=np.arange(1,10,2)
print("1-e:",e)

f=(1,5,2,3,9)
f1 = np.array(f)
print("1-f:",f1)

print(), print()

a21=(1,2,1,5,4)
a22=(1,2,3,4,5)
aa21=np.array(a21)
aa22=np.array(a22)
print("2-a:",aa21+aa22)

b21=(1,2,3,4,5)
b22=(5,4,3,2,1)
bb21=np.array(b21)
bb22=np.array(b22)
print("2-b:",bb21+bb22)

c21=(3,3,3,3,3,3,3,3,3)
cc21=np.array(c21)   
cc22=np.ones(9)                     #array만 쓰라 하셨는데 결과값이 int로 나와서 float로 나오는 ones를 써봤습니다..
print("2-c:",cc21-cc22)             #dtype 변화는 하지않는게 좋을거같았습니다.

d21=(4,5,6)
d22=(3,2,1)
dd21=np.array(d21)
dd22=np.array(d22)
print("2-d:",dd21-dd22)

ee21=np.ones(4)
print("2-e:",2*ee21)                
                                   
f21=(0,4,2,3)
ff21=np.array(f21)
print("2-f:",3*ff21)

g21=(2,4,6,8,10)
gg22=np.array(g21)
print("2-g:",gg22*1/2)

print(), print()

vectora=[1,2,3]
vectorb=[9,8,7]
def dot_product1(vectora, vectorb):
    dotc0=vectora[0]*vectorb[0]
    dotc1=vectora[1]*vectorb[1]
    dotc2=vectora[2]*vectorb[2]
    vectorc1=dotc0+dotc1+dotc2
    return vectorc1
print("3-a:",dot_product1(vectora, vectorb))

def dot_product2(vectora, vectorb):
    vectora2=np.array(vectora)
    vectorb2=np.array(vectorb)
    vectorc2=vectora2*vectorb2
    vectord2=np.sum(vectorc2)
    return vectord2
print("3-b:",dot_product2(vectora, vectorb))

print(), print()

vc=(6,2,4)
def vec_size(vvcvcc):
    vectorc3=np.array(vvcvcc)
    haha=np.sum(vectorc3**2)
    return haha**0.5
print("4:",vec_size(vc))

def vec_size2(vvcvcc):                        #5번문제에서 쓰일 함수
    vectorc33=np.array(vvcvcc)
    haha2=np.sum(vectorc33**2)
    return haha2
print(), print()

# a coordinate
ax = (1,0,0)
ay = (0,1,0)
az = (0,0,1)
# b coordinate
bx = (-2,1,4)
by = (1,2,0)
bz = (2, -1, 1.25)

ax1=np.array(ax)
ay1=np.array(ay)
az1=np.array(az)
bx1=np.array(bx)
by1=np.array(by)
bz1=np.array(bz)

aaxy=np.sum(ax1*ay1)
aaxz=np.sum(ax1*az1)
aayz=np.sum(ay1*az1)
aaxx=np.sum(ax1*ax1)
bbxy=np.sum(bx1*by1)
bbxz=np.sum(bx1*bz1)
bbyz=np.sum(by1*bz1)
bbxx=np.sum(bx1*bx1)
print("5-a:",aaxy,aaxz,aayz,aaxx)
print("5-b:",bbxy,bbxz,bbyz,bbxx)
w1=(6,4,2)
w2=(1,0,0)
w3=(2,2,2)
w4=(1,2,3)
w5=(4,1,7)
w6=(0,-1,2)
ww1=np.array(w1)
ww2=np.array(w2)
ww3=np.array(w3)
ww4=np.array(w4)
ww5=np.array(w5)
ww6=np.array(w6)

def wowwow(wow1, basis):
    hoho=np.sum(wow1*basis)                   #여기서 나오는값이 상수 k이고  기저(x,y,z)에 곱해주면 투영된 좌표 나온다.
    return hoho/(vec_size2(basis))            #투영된 좌표 3개를 모두더하면 다시 원래 벡터값나옴

ccxc1=(ax1*w1[0]+ay1*w1[1]+az1*w1[2])         #coordinate a 에서의 벡터c 뜻이란 a의 기저벡터 3개를 x,y,z라 하고 벡터 c를(x1,y1,z1)이라했을때
ccxc2=(ax1*w2[0]+ay1*w2[1]+az1*w2[2])         #x방향으로 x1만큼 y방향으로 y1만큼 이런 뜻이다 문제에서 coordinate b 에서 (1,2,3) 이란
ccxc3=(ax1*w3[0]+ay1*w3[1]+az1*w3[2])         #xb방향으로 1만큼 xy방향으로 2만큼... 뜻이다.   각각의 기저벡터에서의x,y,z값끼리 모두 더해서 나온 벡터를
ccxc4=(bx1*w4[0]+by1*w4[1]+bz1*w4[2])         #coordinate a 기저벡터들에게 모두 투영시키고 더하면 a에서의 벡터로 나온다.. 제가 잘 이해했는지 모르겠습니다. 
ccxc5=(bx1*w5[0]+by1*w5[1]+bz1*w5[2])
ccxc6=(bx1*w6[0]+by1*w6[1]+bz1*w6[2])
ccx1=np.array(ccxc1)
ccx2=np.array(ccxc2)
ccx3=np.array(ccxc3)
ccx4=np.array(ccxc4)
ccx5=np.array(ccxc5)
ccx6=np.array(ccxc6)


print("5-c:",wowwow(ccx1,bx1),wowwow(ccx1,by1),wowwow(ccx1,bz1))
print("5-d:",format(wowwow(ccx2,bx1),"0.2f"),format(wowwow(ccx2,by1),"0.2f"),format(wowwow(ccx2,bz1),"0.2f"))
print("5-e:",format(wowwow(ccx3,bx1),"0.2f"),format(wowwow(ccx3,by1),"0.2f"),format(wowwow(ccx3,bz1),"0.2f"))
print("5-f:",wowwow(ccx4,ax1),wowwow(ccx4,ay1),wowwow(ccx4,az1))
print("5-g:",wowwow(ccx5,ax1),wowwow(ccx5,ay1),wowwow(ccx5,az1))
print("5-h:",wowwow(ccx6,ax1),wowwow(ccx6,ay1),wowwow(ccx6,az1))




























