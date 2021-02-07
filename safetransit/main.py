from graph import * 

graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
print(graph.vertices)
graph.add_edge("A","B", 12, ["165","166"])
print(graph.adjacency_matrix)
print(graph.transitlines_matrix)
