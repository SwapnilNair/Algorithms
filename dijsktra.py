def dijkstra(WMat,s):
	#Store rows cols and x which is 0 or 1. x isn't even used here
	(rows,cols,x) = WMat.shape
	#Crude estimate of Infinity by multiplying rows * max value in matrix and then just throwing in a plus one for fun
	infinity = max(WMat) * rows + 1
	#Set every vertex to not visited and distance to infinity
	for v in range(rows):
		(visited[v],distance[v]) = (False,infinity)
	#Distance to source is zero as we are starting from it
	(distance[s],visited[s]) = (0,0)
	#For u in rows
	for u in range(rows):
		#next destination is the shortest distance from the current depot to any adjacent depot
		nextd = min([distance[v] for v in range(rows) if not visited[v]])
		#next visitlist is the list of all depots that are at nextd distance away from the current depot
		#and are unvisited
		nextvlit = [v for v in range(rows) if not visited[v] and distance[v]==nextd]
		#If list of depots to visit next is empty,break the algo cause the distances have been found
		if nextvlist = []:
			break
		#Pick the depot with min value from nextvlist
		nextv = min(nextvlist)
		visited[nextv] = True
		#Update the distances to each depot now
		#The new distance is minimum of(currently available distance, distance of the edge from the current vertex)
		for v in range(cols):
			if WMat[nextv,v,0]==1 and (not visited[v]):
				distance[v] =min(distance[v],distance[v]+WMat[next,v,1])
	return distance 

