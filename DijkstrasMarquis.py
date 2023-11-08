""""***************************************************************
* Name       : DijkstrasMarquis
* Author      : Skyler Marquis
* Created    : 11/7/2023
* Course     : CIS 152 - Data Structures and Algorithms  12815-13618
* Version     : 1.0
* OS            : Windows 11
* IDE           : Visual Studio 2022
* Copyright   : This is my own original work based on
*               specifications issued by our instructor
* Description : Use Dijkstra's method to find shortest paths from a single source point in a graph
*               Input: Input graph provided by instructor
*               Output: Shortest paths from source to each vertice
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************"""

# Dijkstra's Algorithm to find the shortest paths from a certain vertex


class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
						for row in range(vertices)]
		self.V_names = [range(vertices)]

	def print_solution(self, dist):
		print("Vertex \tDistance from Source")
		for node in range(self.V):
			print(self.V_names[node], "\t", dist[node])

	# A utility function to find the vertex with minimum distance value, from the set of vertices
	# not yet included in the shortest path tree
	def min_distance(self, dist, spt_set):

		# Initialize minimum distance for next node as incredibly large number
		min_distance = float('inf')

		# Search for the nearest vertex not in the shortest path tree
		for u in range(self.V):
			if dist[u] < min_distance and not spt_set[u]:
				min_distance = dist[u]
				min_index = u

		return min_index

	# Function that implements Dijkstra's single source the shortest path algorithm for a graph represented
	# using adjacency matrix representation
	def dijkstra(self, src):
		try:
			src_element = self.V_names.index(src)
			dist = [float('inf')] * self.V
			dist[src_element] = 0
			spt_set = [False] * self.V

			for cout in range(self.V):

				# Pick the minimum distance vertex from the set of vertices not yet processed.
				# x is always equal to src in first iteration
				x = self.min_distance(dist, spt_set)

				# Put the minimum distance vertex in the shortest path tree
				spt_set[x] = True

				# Update dist value of the adjacent vertices of the picked vertex only if the current
				# distance is greater than new distance and the vertex in not in the shortest path tree
				for y in range(self.V):
					if self.graph[x][y] > 0 and spt_set[y] == False and \
							dist[y] > dist[x] + self.graph[x][y]:
						dist[y] = dist[x] + self.graph[x][y]

			self.print_solution(dist)
		except:
			raise Exception("Source value not found in vertices names")


# Main Driver code
if __name__ == "__main__":
	g = Graph(10)
	g.graph = [[0, 0, 0, 0, 3, 0, 0, 2, 0, 0],
			[0, 0, 0, 0, 0, 2, 0, 0, 0, 7],
			[0, 0, 0, 0, 0, 2, 0, 0, 0, 4],
			[0, 0, 0, 0, 0, 0, 2, 2, 0, 0],
			[3, 0, 0, 0, 0, 0, 3, 3, 0, 0],
			[0, 2, 0, 0, 0, 0, 4, 0, 2, 0],
			[0, 0, 0, 2, 3, 4, 0, 0, 0, 0],
			[2, 0, 0, 2, 3, 0, 0, 0, 0, 3],
			[0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
			[0, 7, 4, 0, 0, 0, 0, 3, 0, 0]]
	g.V_names = ["A", "C", "F", "G", "H", "N", "P", "Q", "R", "T"]

	g.dijkstra("A")
