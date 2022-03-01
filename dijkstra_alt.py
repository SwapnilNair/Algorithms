def dijkstra(WList,s):
	#Define the value of infinity in this context as the number of elements in the list * max distance + 1
	infinity = len(WList.keys()) * max([d for x in WList.keys() for (v,d) in WList[x]]) + 1
	#Initialize visited and distance dictionaries
	(visited,distance) = ({},{})
	#Fill in the values for the vertices
	for v in WList.keys():
		(visited[v],distance[v]) = (False,infinity)
	#Distance to source is zero
	distance[s] = 0
	#For all the vertices:
	for u in WList.keys():
		#Find the distance to the next closest vertex
		nextd = min([distance[v] for v in WList.keys() if not visited[v]])
		#Find the vertices at nextd distance away and not visited
		nextvlist = [v for v in Wlist.keys() if distance[v] == nextd and (not visited[v])]
		#If nextvlist is empty,terminate
		if nextvlist = []:
			break
		#Set nextv as the minimum of nextvlist
		nextv = min(nextvlist)
		visited[nextv]= True
		#For every vertex ,update the newfound distance values
		for(v,d) in WList[nextv]:
			if not visited[v]:
				distance[v] = min(distance[v],distance[nextv])
	return distance
