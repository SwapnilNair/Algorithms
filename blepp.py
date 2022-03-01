def Bin(L,start,end,x,k):
    if end > start:
        mid = (start+end)//2
        if (x==L[mid]):
            j = mid
            i = mid
            while(i>-1 and L[i]==x):
                i-=1
            while(j<k and L[j]==x):
                j+=1
            return(i,j)
            
        elif x<L[mid]:
            return Bin(L,start,mid-1,x,k)
        else:
            return Bin(L,mid+1,end,x,k)
    else:
        return (-22,-22)

def findOccOf(L,x):
    (start,end) = Bin(L,0,len(L),x,len(L))
    if start == -22:
        return(None,None)
    else:
        return(start+1,end-1)
    
    
A = [int(item) for item in input().split(" ")]
x = int(input())
print(findOccOf(A,x))
