from graph import * 

graph = Graph(["A","B","C"],[["B","C",12,["165","166","369"]],["A","B",12,["165","166","369"]]])
print(graph.calculate_penalty(["165"],["165"," 166"]))
print(graph.calculate_penalty(["165"],["166"]))
# graph.add_vertex("A")
# graph.add_vertex("B")
print(graph.vertices)
print(graph.adjacency_matrix)
print(graph.transitlines_matrix)
