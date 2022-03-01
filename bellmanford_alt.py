def bellmanfords(WList,s):
	#Setting up the concept of infinity in this context
	infinity = len(WList.keys())* max([d for x in WList.keys for (v,d) in WList[x]])+1
	#Distance dictionary
	distance = {}
	#Initialize distance of each vertex as infinity
	for v in WList.keys():
		distance[v] = infinity
	#Now the triple decker loop. Distance is either the existing dist or the dist from current vertex to the aid vertex
	for i in WList.keys():
		for u in WList.keys():
			for (v,d) in WList[u]:
				distance[v] = min(distance[v],distance[u]+d)
	return distance
