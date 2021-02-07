class Graph(object):
    nb_vertices = 0
    vertices = []
    adjacency_matrix = []
    transitlines_matrix = []

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
            self.transitlines_matrix[i][j]=lines
            self.adjacency_matrix[i][j]=distance 
