def MoM(L):
    if (len(L)<=3):
        L.sort()
        return L[len(L)//2]
    M = []
    for i in range(0,len(L),3):
        X = L[i:i+3]
        X.sort()
        print(X)
        M.append(X[len(X)//2])
    return MoM(M)


arr=[int(item) for item in input().split(" ")]

print(MoM(arr))
