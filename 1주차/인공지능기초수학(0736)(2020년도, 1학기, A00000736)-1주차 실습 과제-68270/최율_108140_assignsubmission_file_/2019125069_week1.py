import numpy as np
import math

# 1번 문제
firarr1 = np.ones(5)
firarr2 = np.zeros(5)
firarr3 = np.full(5,5)
firarr4 = np.arange(1,6,1)
firarr5 = np.arange(1,10,2)
firarr6 = np.array([1,5,2,3,9])

print("1-a: " , firarr1)
print("1-b: " , firarr2)
print("1-c: " , firarr3)
print("1-d: " , firarr4)
print("1-e: " , firarr5)
print("1-f: " , firarr6)
print("\n")

#2번 문제
secarr1 = np.array([1,2,1,5,4]) + np.arange(1,6,1)
secarr2 = np.arange(1,6,1) + np.arange(5,0,-1)
secarr3 = np.full(9,3) - np.full(9,1)
secarr4 = np.array([4,5,6]) - np.array([3,2,1])
secarr5 = 2 * np.ones(4)
secarr6 = 3 * np.array([0,4,2,3])
secarr7 = 1/2 * np.arange(2,12,2)

print("2-a :" , secarr1)
print("2-b :" , secarr2)
print("2-c :" , secarr3)
print("2-d :" , secarr4)
print("2-e :" , secarr5)
print("2-f :" , secarr6)
print("2-g :" , secarr7)
print("\n")

#3번 문제

#3-a)
a = [1,2,3]
b = [9,8,7]

def DP(a,b):
    if (len(a)!=len(b)):
        print("Invaild Parameter")
        return -1
    else:
        ans = 0
        for i in range(0,len(a)):
            ans += a[i] * b[i]
        return ans
    
print("3-a: " , DP(a,b))

#3-b)
a = np.array([1,2,3])
b = np.array([9,8,7])
c = a * b

print("3-b: " , np.sum(c))
print("\n")


#4번 문제
def vec_size(vec):
    temp = vec * vec
    ans = np.sum(temp)
    ans = math.sqrt(ans)
    return ans

forarr = np.array([6,2,4])
print("4: " , vec_size(forarr))
print("\n")

#5번 문제
def chbas(tag,bas):
    return np.dot(tag,bas)/vec_size(bas)**2
def roundvec(vec):
    vec[0] = round(vec[0],2)
    vec[1] = round(vec[1],2)
    vec[2] = round(vec[2],2)
    

ax = np.array([1,0,0])
ay = np.array([0,1,0])
az = np.array([0,0,1])

bx = np.array([-2,1,4])
by = np.array([1,2,0])
bz = np.array([2,-1,1.25])

fifarr1 = np.array([6,4,2])
fifarr1ans = np.array([chbas(fifarr1,bx),chbas(fifarr1,by),chbas(fifarr1,bz)])
roundvec(fifarr1ans)

fifarr2 = np.array([1,0,0])
fifarr2ans = np.array([chbas(fifarr2,bx),chbas(fifarr2,by),chbas(fifarr2,bz)])
roundvec(fifarr2ans)

fifarr3 = np.array([2,2,2])
fifarr3ans = np.array([chbas(fifarr3,bx),chbas(fifarr3,by),chbas(fifarr3,bz)])
roundvec(fifarr3ans)

fifarr4 = np.array([1,2,3])
fifarr4ans = np.array([chbas(fifarr4,ax),chbas(fifarr4,ay),chbas(fifarr4,az)])
roundvec(fifarr4ans)

fifarr5 = np.array([4,1,7])
fifarr5ans = np.array([chbas(fifarr5,ax),chbas(fifarr5,ay),chbas(fifarr5,az)])
roundvec(fifarr5ans)

fifarr6 = np.array([0,-1,2])
fifarr6ans = np.array([chbas(fifarr6,ax),chbas(fifarr6,ay),chbas(fifarr6,az)])
roundvec(fifarr6ans)

print("5-a: ", np.sum(ax*ay),' ', np.sum(ax*az),' ', np.sum(ay*az),' ',np.sum(ax*ax))
print("5-b: ", np.sum(bx*by),' ', np.sum(bx*bz),' ', np.sum(by*bz),' ',np.sum(bx*bx))
print("5-c: ",fifarr1ans)
print("5-d: ",fifarr2ans)
print("5-e: ",fifarr3ans)
print("5-f: ",fifarr4ans)
print("5-g: ",fifarr5ans)
print("5-h: ",fifarr6ans)
