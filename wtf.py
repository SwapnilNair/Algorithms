'''
def Merge(A,B):
    (m,n) = (len(A),len(B))
    (C,i,j,k) = ([],0,0,0)
    while k < m+n :
        if i == m:
            C.extend(B[j:])
            k = k + n - j
        elif j == n :
            C.extend(A[i:])
            k = k + m -i
        elif A[i] < B[j]:
            C.append(A[i])
            (k,i) = (k+1,i+1)
        else:
            C.append(B[j])
            (k,j) = (k+1,j+1)
    return C
        
        
def sortInRange(L,r):
    n = len(L)
    if n<=1:
        return L
    else:
        Left = sortInRange(L[:n//2],r)
        Right = sortInRange(L[n//2:],r)
        B = Merge(Left,Right)
    return B

L = [9,8,3,5,1,4,0,7,6,5,4,3,2,1,0]
print(sortInRange(L,10))
'''
def sortInRange(L,r):
    vals = {}
    for i in range(r):
        vals[i] = 0
    for x in L:
        vals[x] = vals[x]+1
    P = []
    for x in vals.keys():
        for y in range(vals[x]):
            P.append(x)
    return P    

K = [1,2,2,3,3,4,3,4,3,0,0,3,0,0,4,3,4,2,0,1,1,1,3,2]
print(sortInRange(K,5))
