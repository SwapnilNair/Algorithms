# Merge Sort

#First the function that merges the list
def Merge(A,B):
	(m,n) = (len(A),len(B))
	(C,i,j,k) = ([],0,0,0)
	while k<m+n:
		#If first list has been gone over
		if i == m:
			C.extend(B[j:])
			k = k + n - j
		elif j == n:
			C.extend(A[i:])
			k = k + m - i
		elif A[i] < B[j]:
			C.append(A[i])
			k+=1
			i+=1
		else:
			C.append(B[i])
			k+=1
			j+=1
	return(C)

# Recursive mergesort function
def mergesort(A):
	n = len(A)
	if n<=1 :
		return A
	else:
		L = mergesort(A[0:n//2])
		R = mergesort(A[n//2:])
		B = Merge(L,R)
	return(B)

L = [1,4,3,56,239,8,7,0]
print(mergesort(L))
