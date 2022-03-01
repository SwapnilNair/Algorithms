'''def gcd1(m,n):
    (a,b)=(max(m,n),min(m,n));
    if a%b ==0:
        return b;
    else:
        return gcd1(b,a-b);

#Euclid's Algorithm
#Proportional to number of digits
def gcd2(m,n):
    (a,b)=(max(m,n),min(m,n));
    if a%b ==0:
        return(b)
    else:
        return gcd2(b,a%b);

print(gcd1(10,1003));

__str__(){
    #implicitly called by print
}'''

import random as rd;
import time
'''
start = time.perf_counter()
f = open("input_file_s","w")
i=0
for i in range(10000):
    string='';
    for j in range(31):
        string += str(rd.randint(0,1));
    f.write(string+"\n")
end=time.perf_counter();
print("Time elapsed: ",end-start)
'''

def is_Prime(x):
    if(x==1):return False
    if(x%2==0):
        return False
    else:
        for i in range(3,int(x**0.5 )+1,2):
            if x%i ==0:
                return False
    return True
'''
def is_Prime(x):
    for i in range(2,int(x**0.5+1)):
        if(x%i==0):
            return False
    return True
    '''

'''
def Twin_Primes(n,m):
    l = []
    if(n%2==0):
        for i in range(n+1,m+1,2):
            if(is_Prime(i) and is_Prime(i+2)):
                l.append((i,i+2))
    else:
        for i in range(n,m+1,2):
            if(is_Prime(i) and is_Prime(i+2)):
                l.append((i,i+2))
    return l
'''

start = time.perf_counter();
print(is_Prime(10000000000))
print(is_Prime(122352))
print(is_Prime(1726331769))
print(is_Prime(73939133))
print(is_Prime(23513892331597))
end = time.perf_counter();
print(end-start)
class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def is_valid(self):
        if(self.a+self.b>self.c and self.a+self.c>self.b and self.b+self.c>self.a):
            self.validity = "Valid"
            return True
        self.validity = "Invalid"
        return Invalid
    def Side_Classification(self):
        if(self.validity == "Invalid"):
            return "Invalid"
        else:
            if(self.a == self.b == self.c):
                return "Equilateral"
            elif(self.a!=self.b and self.b!=self.c and self.c!=self.a):
                return "Scalene"
            else:
                return "Isosceles"
    def Angle_Classification(self):
        pass
    def Area(self):
        pass