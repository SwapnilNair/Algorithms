def kruskal(WList):
	#Dictionary for components and lists for Tree Edges and edges
	(edges,component,TE) = ([],{},[])
	#For every vertex
	for u in WList.keys():
		#Add all edges present in the graph
		edges.extend([(d,u,v) for (v,d) in WList(u)])
		#Mark all of them as distinct and independent components
		component[u] = u
	#Sort the list of edges in order
	edges.sort()

	for (d,u,v) in edges:
		#If u and v are separate components add the edge from u to v
		if component[u] != component[v]:
			TE.append((u,v))
			#Hold the component number of u in c. For all the vertices, if component number was u, change to v
			c  = component[u]
			for x in WList.keys():
				if component[x] == c:
					component[x] = v
	return TE



