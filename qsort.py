#This is my attempt at learning quicksort
def quicksort(L,l,r):
	if(r-l <=1):
		return L
	(pivot,lower,upper) = (L[l],l+1,l+1)
	for i in range(l+1,r):
		if L[i] > pivot:
			upper+=1
		else:
			#swap the lower vlaue of upper with the current element,increment both upper and lower
			(L[lower],L[i]) = (L[i],L[lower])
			(lower,upper) = (lower+1,upper+1)
	#Put pivot at the middle
	(L[l],L[lower-1]) = (L[lower-1],L[l])
	lower -=1
	
	quicksort(L,l,lower)
	quicksort(L,l+1,upper)
	return L


import random
import time
import sys

sys.setrecursionlimit(2**31-1)

X = [random.randrange(10000)for i in range(10)]
print(X)
start = time.time()
quicksort(X,0,len(X))
end = time.time()
print(X)
print(end-start)
