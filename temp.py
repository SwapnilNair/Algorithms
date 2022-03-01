def toposort(alist):
	(indegree,toposortlist) = ({},[])
	for u in alist.keys():
		indegree[u] = 0
	for u in alist.keys():
		for v in alist[u]:
			indegree[v] = indegree[v]+1

	zerodegreeq = Queue()
	for u in alist.keys():
		if indegree[u] == 0:
			zerodegreeq.addq(u)

	while(not zerodegreeq.isempty()):
		j = zerodegreeq.delq()
		toposortlist.append(j)
		indegree[j] = indegree[j]-1
		for k in alist[j]:
			indegree[k] = indegree[k]-1
			if(indegree[k] ==0):
				zerodegreequeue.addq(k)
	return toposortlist


'''
def toposort(adjmat):
	(rows,cols) = adjmat.size
	indegree={}
	toposortlist = []

	#Make a dict with each vertex and its indegree
	for c in range(cols):
		indegree[c] = 0
		for r in range(rows):
			if adjmat[r][c] ==1:
				indegree[c] = indegree[c]+1
	for i in range(rows): 
		#Find the vertices with zero indegree
		j = min([x for x in range(cols) if indegree[x] ==0])
		#Add the said vertex to the output list
		toposortlist.append(j)
		#Change that indegree of that vertex to 0
		indegree[j] = indegree[j]-1
		#Reduce indegrees of all vertices 
		for x in range(cols):
			if adjmat[j][x] ==1:
				indegree[x] = indegree[x] - 1
	return toposortlist
'''

