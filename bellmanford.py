def bellmanford(WMat,s):
	(rows,cols,x) = np.WMat.shape
	#defining infinity in this context
	infinity = np.max(WMat)* rows + 1
	#Distance dictionary
	distance = {}
	#initializing all vertices to zero
	for v in WMat.keys():
		distance[v] = infinity
	#Distance of source vertex is 0
	distance[s] = 0
	#Triple decker loop :)
	for i in range(rows):
		for u in range(rows):
			for v in range(cols):
				if WMat[u,v,0] == 1:
					distance[v] = min(distance[v],distance[u] + WMat[u,v,1])
	return distance
