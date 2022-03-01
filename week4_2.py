def DFSInit(adjMAT):
	(rows,cols) = adjMAT.shape
	(visited,parents) = ({},{})
	for i in range rows:
	visited[i] = False
	parents[i] = -1
	return (visited,parents)

def DFS(adjMAT,visited,parent,v):
	visited[v] = True
	for k in neighbours(v):
		if (not visited[k]):
			parent[k] = v
			(visited,parent) = DFS(adjMAT,visited,parent,k)
 	return (visited,parent)
