def prims(WList):
	#Defining the conceot of infinity in this scope
	infinity = max([d for x in WList.keys() for (v,d) in Wlist[x]])
	#Create visited,distance dictionaries and a list of edges
	(visited,distance,TreeEdges) = ({},{},[])
	#Set distance to each vertex as infinity and visited as false
	for v in WList.keys():
		(visited[v],distance[v]) = (False,infinity)
	#Set first vertex as visited
	visited[0] = True
	#Set distance of each neighbour of node[0] according to the adjacency list
	for (v,d) in WList[0]:
		distance[v] = d
	#for every vertex in the list, set mindist to inf and nextv to none
	for i in WList.keys():
		(mindist,nextv) = (infinity,None)
		#for every vertex u in the list, for every v,d in its adjacency list,
		#If u has been visited and v is the unvisited nearest vertex with d<mindist,set that as the nextv
		for u in WList.keys():
			for (v,d) in Wlist[u]:
				if visited[u] and not visited[v] and d<mindist:
					(mindist,nextv,nexte) = (d,v,(u,v))
		if nextv is None:
			break
		#set next vertex as visited add it to the TreeEdgeslist
		visited[nextv]=True
		TreeEdges.append(nextv)
		#for every vertex v in nextv's adjacency list, set distance of v as minimum of distance[v] and d
		for (v,d) in Wlist[nextv]:
			if not visited(v):
				distance[v] = min(distance[v],d)
	return TreeEdges
