def prims_alt(WList):
	#Concept of infinity
	infinity = max([d for x in WList.keys() for (v,d) in WList[x]]+1
	(visited,distance,nbr) = ({},{},{})
	#Visited ,distance and neighbour dictionaries
	for v in WList.keys():
		(visited[v],distance[v],nbr[v]) = (False,infinity,-1)
	#Set first vertex as visited
	visited[0] = True
	#
	for(v,d) in  WList[0]:
		(distance[v],nbr[v]) = (d,0)

	for i in range(1,len(WList.keys())):
		nextd = min([distance[v] for v in WList.keys() if not visited[v]])
		nextvlist = [v fo v in WList.keys() if not visited[v] and distance[v] == nextd]
	if nextvlist = []:
		break
	nextv = min(nextvlist)
	visited[nextv] = True
	for (v,d) in WList[nextv]:
		if not visited[v]:
			(distance[v],nbr[v]) = (min(distance[v],d),nextv)
	return nbr
