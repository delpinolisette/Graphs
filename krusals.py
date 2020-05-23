# krusals.py
# this is my implementation of Krusal's Greedy Algorithm 
# to find a minimal spanning tree 

# source : https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

 from collections import defaultdict

 #build the graph class , the grpah object with its methods
 class Graph
 	#constructor
 	def _init_(self, vertices): #if you pass in self you can assign attributes, in later methods you can access them
 		self.V = vertices #number of vertices of graph. 
 		self.graph = [] #default dictionary to store the graph 

 	#adds an edge to the graph, how is u,v,w an edge?
 	def addEdge(self, u,v,w):
 		self.graph.append([u,v,w])

