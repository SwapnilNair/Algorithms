def floydwarshall(WMat):
	#The shape of the matrix
	(rows,cols,x) = WMat.shape
	#infinity to be defined
	infinity = np.max(WMat)+1
	#A matrix with size N*N*N+1
	SP = np.zeroes(shape = (rows,cols,cols+1))
	#Initialize all of the distances to infinity
	for i in range(rows):
		for j in range(cols):
			SP[i,j,0] = infinity

	#Fill in all the distances where A to B is a direct edge
	for i in range(rows):
		for j in range(cols):
			if WMat[i,j,0] ==1:
				SP[i,j,0] = WMat[i,j,1] #0 is for the edgeand 1 is for the distance
	#Loop from 1 to k+1
	#for i j in rows and columns,
	#distance from i to j is either curr distance or sum of distance from i to k-1 and  k-1 to j
	for k in range(1,cols+1):
		for i in range(rows):
			for j in range(cols):
				SP[i,j,k] = min(SP[i,j,k-1],SP[i,k-1,k-1]+SP[j,k-1,k-1])
	#Return the last matrix slice only, the rest have no use
	return (SP[:,:,cols])
