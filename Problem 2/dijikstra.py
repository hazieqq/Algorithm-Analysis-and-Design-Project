from collections import defaultdict


class Graph:

	def __init__(self,s,l):
			self.s=s
			self.l=l
	
	def minDistance(self,dist,queue):
		minimum = float("Inf")
		min_index = -1
		
		for i in range(len(dist)):
			if dist[i] < minimum and i in queue:
				minimum = dist[i]
				min_index = i
		return min_index

	def printPath(self, parent, j):
    		
		if parent[j] == -1:
			self.s = self.s + str(j)
			return str(self.s)
			
		self.printPath(parent , parent[j])
		self.s = self.s + str(j)
		self.l.append(self.s)
	
	def printSolution(self, dist, parent):
		src = 0
		self.l.append(dist[2])
		self.printPath(parent,2)
		return self.l
		
	def dijkstra(self, graph, src):

		row = len(graph)
		col = len(graph[0])

		dist = [float("Inf")] * row

		parent = [-1] * row
		
		dist[src] = 0
	
		queue = []
		for i in range(row):
			queue.append(i)
		while queue:
		
			u = self.minDistance(dist,queue)

			queue.remove(u)

			for i in range(col):
				if graph[u][i] and i in queue:
					if dist[u] + graph[u][i] < dist[i]:
						dist[i] = dist[u] + graph[u][i]
						parent[i] = u

		b=self.printSolution(dist,parent)
		return b