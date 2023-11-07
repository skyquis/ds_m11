# Dijkstra's Algorithm to find the shortest paths from a certain vertex

# Python program for Dijkstra's single source the shortest path algorithm.

# Import sys library
import sys


class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
						for row in range(vertices)]

	def print_solution(self, dist):
		print("Vertex \tDistance from Source")
		for node in range(self.V):
			print(node, "\t", dist[node])

	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in the shortest path tree
	def min_distance(self, dist, spt_set):

		# Initialize minimum distance for next node
		min_distance = sys.maxsize

		# Search for the nearest vertex not in the shortest path tree
		for u in range(self.V):
			if dist[u] < min_distance and spt_set[u] == False:
				min_distance = dist[u]
				min_index = u

		return min_index

	# Function that implements Dijkstra's single source
	# the shortest path algorithm for a graph represented
	# using adjacency matrix representation
	def dijkstra(self, src):

		dist = [sys.maxsize] * self.V
		dist[src] = 0
		spt_set = [False] * self.V

		for cout in range(self.V):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# x is always equal to src in first iteration
			x = self.min_distance(dist, spt_set)

			# Put the minimum distance vertex in the
			# shortest path tree
			spt_set[x] = True

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current
			# distance is greater than new distance and
			# the vertex in not in the shortest path tree
			for y in range(self.V):
				if self.graph[x][y] > 0 and spt_set[y] == False and \
						dist[y] > dist[x] + self.graph[x][y]:
					dist[y] = dist[x] + self.graph[x][y]

		self.print_solution(dist)


# Driver's code
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

	g.dijkstra(0)

# This code is contributed by Divyanshu Mehta and Updated by Pranav Singh Sambyal
