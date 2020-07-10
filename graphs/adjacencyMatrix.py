import logging
from copy import copy, deepcopy

logging.basicConfig(filename='myMatrixGraph.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of the program')

class Vertex():
    def __init__(self, n):
        self.name = n

class Graph():
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            # Creating 2 by 2 matrix of edges
            self.edges = [[0 for x in range(len(self.edges) + 1)] for y in range(len(self.edges) + 1)] 
            # for row in self.edges:
            #     row.append(0)
            logging.debug('Edges %s' % (self.edges))
            # self.edges.append([0] * (len(self.edges) + 1))
            # logging.debug('Edges column? %s' % (self.edges))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            logging.debug('Edge indices %s' % (self.edge_indices))
            return True
        else:
            return False

    def add_edge(self, u, v, weight = 1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end = '')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end='')
            print(' ')

g = Graph()
c = Vertex('C')
g.add_vertex(c)
g.add_vertex(Vertex('A'))
for i in range(ord('A'), ord('L')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()
