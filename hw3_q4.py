#CSE 373 - Homework 3 Question 4A

# first number = number of edges
# second number = number of vertices
# each line = edge between the pair of numbered vertices
# graph is undirected
import sys
"""
Run graph script on the command line - arg1 = filename
"""
class EdgeNode():
    def __init__(self, y, next_edge=None):
        self.y = y
        self.next = next_edge

    def __str__(self):
        return str(self.y)

class Graph():
    def __init__(self):
        self.num_vertices = 0
        self.num_edges = 0
        self.adjacency_list = []
        self.degree_list = []

    def read_graph(self, file_name):
        f = open(file_name)
        self.num_edges = int(f.readline().strip())
        self.num_vertices = int(f.readline().strip())
        self.adjacency_list = [None]*self.num_vertices
        self.degree_list = [0]*self.num_vertices

        for edge_line in f:
            edge = edge_line.strip().split()
            x = int(edge[0])
            y = int(edge[1])
            self.insert_edge(x, y, False)

        f.close()

    def insert_edge(self, x, y, is_directed):
        edge_node = EdgeNode(y, self.adjacency_list[x - 1])
        self.adjacency_list[x - 1] = edge_node
        self.degree_list[x - 1] += 1

        if(is_directed == False):
            self.insert_edge(y, x, True)

    def print_adjacency_list(self):
        for i in range(0, self.num_vertices):
            print(i + 1, "->", end = " ")
            edge = self.adjacency_list[i]
            while(edge != None):
                print(edge, end =" ")
                edge = edge.next
            print()

    def dfs(self, x):
        if(x in self.discovered):
            return
        self.discovered[x] = True
        print(x, end = ", ")
        edge = self.adjacency_list[x - 1]
        while(edge != None):
            self.dfs(edge.y)
            edge = edge.next
    

    def print_connected_components(self):
        self.discovered = {}
        component_num = 0
        for i in range(0, self.num_vertices):
            x = i + 1
            if(x not in self.discovered):
                component_num += 1
                print("Component", component_num, end=": ")
                self.dfs(i + 1)
                print()



file_name = sys.argv[1] 

graph = Graph()
graph.read_graph(file_name)
# graph.print_adjacency_list()

graph.print_connected_components()