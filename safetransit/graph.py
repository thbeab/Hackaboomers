import sys
import copy

class Graph(object):
    nb_vertices = 0
    vertices = []
    adjacency_matrix = []
    transitlines_matrix = []

    def __init__(self, vertices, edges):

        for vertex in vertices:
            self.add_vertex(vertex)

        for edge in edges:
            v1 = edge[0] 
            v2 = edge[1]
            distance = edge[2]
            lines = edge[3]
            self.add_edge(v1, v2, distance, lines)

    def add_vertex(self, v):
        if(v in self.vertices):
            print("Vertex already exists")
        else :
            self.vertices.append(v)
            self.nb_vertices += 1
        if(self.nb_vertices > 1):
            for vertex in self.transitlines_matrix:
                vertex.append([])
            for vertex1 in self.adjacency_matrix:
                vertex1.append(0)
        temp = []
        for i in range (self.nb_vertices):
            temp.append([])
        self.transitlines_matrix.append(temp)
        temp  = []
        for i in range (self.nb_vertices):
            temp.append(0)
        self.adjacency_matrix.append(temp)

    def add_edge(self, v1, v2, distance, lines):
        if(v1 not in self.vertices):
            print("Vertex ", v1, "does not exist")
        elif(v2 not in self.vertices):
            print("Vertex ", v2, "does not exist")
        else:
            i=self.vertices.index(v1)
            j=self.vertices.index(v2)
            print(i, j)
            self.transitlines_matrix[i][j]=lines
            self.adjacency_matrix[i][j]=distance 

    # fuction that calculates penalty from line changes for Dijkstra algorithm
    def calculate_penalty(self, current_lines, adjacent_lines):
        intersected_lines = []
        penalty = 0
        if((adjacent_lines!=[]) and (current_lines!=[])):
            for l in current_lines:
                if l in adjacent_lines:
                   intersected_lines.append(l)
        if(intersected_lines==[]):
            penalty = 5
            intersected_lines = adjacent_lines

        return [penalty, intersected_lines] 
            
    # shortest path from s
    def modified_dijkstra(self, s):
        cost = []
        path = []
        lines = []
        unvisited =[]

        for v in range(nb_vertices):
            cost[v]=sys.maxsize
            unvisited.append(self.vertices[v])

        cost[self.vertices.index(v)]=0
         
        current = copy.deepcopy(s)

        while(unvisited!=[]):
            for u in unvisited:
                if(cost[u] < cost[current]):
                    current=u
            unvisited.remove(current)
            
            for j in range(nb_vertices):
                if(self.adjacency_matrix[current][j] > 0):
                    intersected_lines = []
                    tmp = self.calculate_penalty(lines[self.vertices.index(current)],transitlines_matrix[current][j])
                    penalty = tmp[1]
                    intersected_lines = tmp[2]
                    alternaative_cost = cost[self.vertices.index(current)] +
                    self.adjacency_matrix[current][j]
                    
                    if(alternaative_cost 
                    



