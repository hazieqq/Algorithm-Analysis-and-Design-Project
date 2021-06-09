# Implementation of Johnson's algorithm in Python3

# Import function to initialize the dictionary
from collections import defaultdict
MAX_INT = float('Inf')
l =[]
# a=[]
# Returns the vertex with minimum
# distance from the source
def minDistance(dist, visited):
    a=[]
    (minimum, minVertex) = (MAX_INT, 0)
    for vertex in range(len(dist)):
        if minimum > dist[vertex] and visited[vertex] == False:
            (minimum, minVertex) = (dist[vertex], vertex)
            a = [minVertex,vertex]
    return a

def printPath(parent, j,s):
    #Base Case : If j is source
    while True:
        if parent[j] == -1:
            s.append(j)
            # print(j)
            return s
            break
        else:
            s.append(j)
            # print(j)
            j = parent[j]
    
    # if parent[j] == -1 : 
    #     s.append(j)
    #     print(j)
    #     return s
    # s.append(j)
    # printPath(parent , parent[j],s)
    # print(j)


def printSolution(dist, parent):
    src = 0
    l=[]
    
    x = printPath(parent,2,l)
    return x[1]
        


def Dijkstra(graph, modifiedGraph, src):

    num_vertices = len(graph)

    parent = [-1] * num_vertices

    
    sptSet = defaultdict(lambda : False)

    dist = [MAX_INT] * num_vertices

    dist[src] = 0
    for count in range(num_vertices):

       
        b = minDistance(dist, sptSet)
        curVertex = b[0]
        sptSet[curVertex] = True

        for vertex in range(num_vertices):
            if ((sptSet[vertex] == False) and
                (dist[vertex] > (dist[curVertex] +
                modifiedGraph[curVertex][vertex])) and
                (graph[curVertex][vertex] != 0)):
                parent[vertex] = curVertex
                dist[vertex] = (dist[curVertex] +
                                modifiedGraph[curVertex][vertex]);

    # Print the Shortest distance from the source
    hub = printSolution(dist,parent)
    for vertex in range(num_vertices):
        if vertex == 2:
            c = [dist[vertex],hub]
            return c
            
        # print ('Vertex ' + str(vertex) + ': ' + str(dist[vertex]))

# Function to calculate shortest distances from source
# to all other vertices using Bellman-Ford algorithm
def BellmanFord(edges, graph, num_vertices):

    # Add a source s and calculate its min
    # distance from every other node
    dist = [MAX_INT] * (num_vertices + 1)
    dist[num_vertices] = 0

    for i in range(num_vertices):
        edges.append([num_vertices, i, 0])

    for i in range(num_vertices):
        for (src, des, weight) in edges:
            if((dist[src] != MAX_INT) and
                    (dist[src] + weight < dist[des])):
                dist[des] = dist[src] + weight

    # Don't send the value for the source added
    return dist[0:num_vertices]

# Function to implement Johnson Algorithm
def JohnsonAlgorithm(graph):

    edges = []

    # Create a list of edges for Bellman-Ford Algorithm
    for i in range(len(graph)):
        for j in range(len(graph[i])):

            if graph[i][j] != 0:
                edges.append([i, j, graph[i][j]])

    # Weights used to modify the original weights
    modifyWeights = BellmanFord(edges, graph, len(graph))

    modifiedGraph = [[0 for x in range(len(graph))] for y in
                    range(len(graph))]

    # Modify the weights to get rid of negative weights
    for i in range(len(graph)):
        for j in range(len(graph[i])):

            if graph[i][j] != 0:
                modifiedGraph[i][j] = (graph[i][j] +
                        modifyWeights[i] - modifyWeights[j]);


    # Run Dijkstra for every vertex as source one by one
    for src in range(1):
        print ('\nShortest Distance with vertex ' +
                        str(src) + ' as the source:\n')
        return Dijkstra(graph, modifiedGraph, src)
        
        

# Driver Code
# graph = [[0,70.2,0,42.8,24.8,75.7,26.8],
# 		[70.2,0,28.8,0,0,0,0],
# 		[0,28.8,0,20.5,36.3,49.2,27.2],
# 		[42.8,0,20.5,0,0,0,0],
#         [24.8,0,36.3,0,0,0,0],
#         [75.7,0,49.2,0,0,0,0],
# 		[26.8,0,27.2,0,0,0,0]
#         ]

# y = JohnsonAlgorithm(graph)
# print(y)
