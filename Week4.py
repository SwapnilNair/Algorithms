# BFS
class Queue :
	def __init__(self):
		self.queue = []
	def addq(self,v):
		self.queue.append(v)
	def delq(self):
		v = None
		if not self.isEmpty():
			v = self.queue[0]
			self.queue = self.queue[1:]
		return v
	def isEmpty(self):
		return (self.queue == [])
	def __str__(self):
		return (str(self.queue))

def BFS(adjmat,v):
	# Rows and coluns are found 
	(rows,cols) = adjmat.shape
	visited = {} # Visited dictionary
	for i in range(rows):
		visited[i] = False # initializing visited dictionary
	q = Queue() # queue to hold the elements visited

	visited[v] = True # set initial element as visited
	q.addq(v) 
	while(not q.isEmpty() ):
		j = q.delq() # serve the queue
		for k in neighbours(adjmat,j): # look at the neighbours and if they are not visited, add them to the queue as well
			if (not visited[k]):
				visited[k] = True
				q.addq(k)
	return (visited)
# BFS that stores path
def BFS(AdjLIST,v):
	(visited,parent) = ({},{}) # Two dictionaries : one for parent and other for BFS navigation
	for i in AdjLIST.keys(): #Initializing the dictionaries
		visited[i] = False
		parent[i] = -1
	q = Queue()
	q.addq(v)
	visited[v] = True # Create and add initial vertex to the queue variable
	while(not q.isEmpty()): # While the queue is not empty, service.
		j = q.delq()
		for k in Adjlist[j]: #For every element in adjacency list of q
			if(not visited[k]):
				visited[k] = True # if not visited add to queue, set as visited and set j as the parent
				parent[k] = j
				q.addq(k)
		return (visited,parent) # return both the dictionaries
