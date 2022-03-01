# Merge Sort {Uses Divide and Conquer Principle}
def Merge(A,B):
	m,n = len(A),len(B)
	(C,i,j,k) = ([],0,0,0)
	while k < m+n:
		# If the first list is exhausted, copy over the rest of the second list
		if i == m:
			C.extend(B[j:i])
			k = k+(n-j)
		# If the first list is exhausted, copy over the rest of the first list
		elif j == n:
			C.extend(A[i:])
			k = k + (n-i)
		# If the first element of the first list is larger, copy it over to the op list 
		elif A[i] < B[j]:
			C.append(A[i])
			(i,k) = (i+1,k+1)
		# If the first element of the second list is larger, copy it over to the op list
		else :
			C.append(B[j])
			(j,k) = (j+1,k+1)
	return(C)

def MergeSort(A):
	n = len(A)
	if n<=1:
		return (A)
	L = MergeSort(A[:n//2])
	R = MergeSort(A[n//2:])
	B = Merge(L,R)
	return(B)

l = [1,4,5,2,0,7,9,18,-3,20]
print(MergeSort(l))
'''
def insertionsort(L):
	n = len(L);
	if n <1 :
		return(L)
	for i in range(n):
		j = i
		print(L[i],L)
		while(j>0 and L[j] < L[j-1]):
			L[j],L[j-1] = L[j-1],L[j]
			j = j-1
	return (L)
X = [1,5,3,9,2]
print(insertionsort(X))
# Put one element in the new list
# Put the next element to the left or right according to the value it has
'''
'''
def selectionsort(L):
	n = len(L)
	if n < 1:
		return L
	for i in range(n):
		mpos = i
		for j in range(i+1,n):
			if L[j] < L[mpos]:
				mpos = j
		L[i],L[mpos] = L[mpos],L[i]
	return L
'''
# select the smallest element from the list
# swap that with the element at the starting position i
# proceed to find the next smallest element and set it as i+1 and so on...
# exit if only one element is there in the list

