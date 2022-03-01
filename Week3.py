# QuickSort
def quicksort(L,l,r):
	#If list has only one element, return the list as is
	if(r-l <=1):
		return L
	# Set pivot as the very first position in the list, upper and lower are the next element
	(pivot,lower,upper) = (L[l],l+1,l+1)
	# Loop from the item after pivot to the end
	for i in range(l+1,r):
		#If L[i] is higher than pivot, upper is incremented
		if L[i] > pivot:
			upper +=1
		else: # exchange L[i] with start of upper segment
			(L[i],L[lower]) = (L[lower],L[i])
			upper +=1
			lower +=1

	#Move pivot to the center of the list

	(L[l],L[lower-1]) = (L[lower-1],L[l])
	lower -=1

	#Recursively sort the LHS and RHS of pivot now
	quicksort(L,l,lower)
	quicksort(L,lower+1,upper)

	#Return the list
	return L

A = [4,5,6,2,3,7,8,9]
print(quicksort(A,0,len(A)))
