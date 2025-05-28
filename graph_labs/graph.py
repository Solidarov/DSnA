from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class UndirectedGraph:
    def __init__(self, vertices):
        vertices = list(dict.fromkeys(vertices))
        self.vertices = {v:i for i, v in enumerate(vertices)}
        self.q_vertices = len(self.vertices.keys())
        self.matrix = [[0] * self.q_vertices for _ in range(self.q_vertices)]

    def add_edge(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            return False
        self.matrix[self.vertices[start]][self.vertices[end]] = 1
        self.matrix[self.vertices[end]][self.vertices[start]] = 1
        return True

    def del_edge(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            return False
        self.matrix[self.vertices[start]][self.vertices[end]] = 0
        self.matrix[self.vertices[end]][self.vertices[start]] = 0
        return True
    
    
    def visualize(self):
        G = nx.Graph()
        
        for v in self.vertices:
            G.add_node(v)
        
        for v1 in self.vertices:
            for v2 in self.vertices:
                i, j = self.vertices[v1], self.vertices[v2]
                if self.matrix[i][j] and i < j:  # Щоб не дублювати ребра
                    G.add_edge(v1, v2)
        nx.draw(G, with_labels=True, node_color='lightblue', edge_color='black')
        plt.show()


    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        result = [start]

        for neighbor in self.vertices:
        
            if self.matrix[self.vertices[start]][self.vertices[neighbor]] and neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        
        return result
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in self.vertices:
                    if self.matrix[self.vertices[vertex]][self.vertices[neighbor]] and neighbor not in visited:
                        queue.append(neighbor)
        return result
