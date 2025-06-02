from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class UndirectedGraph:
    def __init__(self, vertices):
        vertices = list(dict.fromkeys(vertices))
        self.vertices = {v:i for i, v in enumerate(vertices)}
        self.q_vertices = len(self.vertices.keys())
        self.matrix = [[(0,0)] * self.q_vertices for _ in range(self.q_vertices)]

    def add_edge(self, start, end, weight=0):
        if start not in self.vertices or end not in self.vertices:
            return False
        self.matrix[self.vertices[start]][self.vertices[end]] = (1, weight)
        self.matrix[self.vertices[end]][self.vertices[start]] = (1, weight)
        return True

    def del_edge(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            return False
        self.matrix[self.vertices[start]][self.vertices[end]] = (0,0)
        self.matrix[self.vertices[end]][self.vertices[start]] = (0,0)
        return True
    
    
    def visualize(self):
        G = nx.Graph()
        
        for v in self.vertices:
            G.add_node(v)
        
        for v1 in self.vertices:
            for v2 in self.vertices:
                i, j = self.vertices[v1], self.vertices[v2]
                if self.matrix[i][j][0] and i < j:  # Щоб не дублювати ребра
                    G.add_edge(v1, v2, weight=self.matrix[i][j][1])
        
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='black')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels, label_pos=0.5)
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
    
    def kruskal(self):

        edges = []
        for v1 in self.vertices:
            for v2 in self.vertices:
                i, j = self.vertices[v1], self.vertices[v2]
                if self.matrix[i][j][0] and i < j:
                    edges.append((self.matrix[i][j][1], v1, v2))
        
        edges.sort()
        
        parent = {v: v for v in self.vertices}
        
        def find(v):
            while parent[v] != v:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return v
        
        def union(u, v):
            parent[find(u)] = find(v)
        
        mst = []
        for weight, u, v in edges:
            if find(u) != find(v):
                mst.append((u, v, weight))
                union(u, v)

        g = UndirectedGraph([i for i in parent])
        for s, e, w in mst:
            g.add_edge(s, e, w)
        g.visualize()

    def prim(self, start=None):
        
        if start is None:
            start = list(self.vertices.keys())[0]
        
        
        nodes_in_tree = [start]
        
        mst_edges = []
        
        
        while len(nodes_in_tree) < len(self.vertices):
            best_edge = None
            best_weight = float('inf') 
            
            
            for node in nodes_in_tree:
                
                for other_node in self.vertices:
                    
                    if other_node in nodes_in_tree:
                        continue
                    
                    
                    i, j = self.vertices[node], self.vertices[other_node]
                    if self.matrix[i][j][0]:
                        weight = self.matrix[i][j][1]
                        
                        if weight < best_weight:
                            best_weight = weight
                            best_edge = (node, other_node, weight)
            
            if best_edge is None:
                print("Граф не зв'язний! MST є частковим.")
                break
            
            u, v, w = best_edge
            nodes_in_tree.append(v)
            mst_edges.append((u, v, w))
        
        g = UndirectedGraph(list(self.vertices.keys()))
        for u, v, w in mst_edges:
            g.add_edge(u, v, w)
        
        g.visualize()

    def _visualize_paths(self, start, distances, previous):
        msg = f"\nShortest path from vertex {start}:"
        
        for vertex in self.vertices:
            if vertex == start:
                continue
            
            if distances[vertex] == float('inf'):
                msg += f"\n\tTo {vertex}: doesnt have path"
            else:
                path = []
                current = vertex
                while current is not None:
                    path.append(current)
                    current = previous[current]
                path.reverse()
                
                msg += f"\n\tTo {vertex}: {' -> '.join(path)}, distance  = {distances[vertex]}"
        return msg

    def dijkstra(self, start=None):
        if start is None:
            start = min(self.vertices.keys(), key=lambda v: self.vertices[v])

        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        
        previous = {vertex: None for vertex in self.vertices}
        
        unvisited = set(self.vertices)
        
        while unvisited:
            current = min(unvisited, key=lambda v: distances[v])
            
            if distances[current] == float('inf'):
                break
                
            unvisited.remove(current)
            
            for neighbor in self.vertices:
                i, j = self.vertices[current], self.vertices[neighbor]
                if not self.matrix[i][j][0]:
                    continue
                    
                weight = self.matrix[i][j][1]
                new_distance = distances[current] + weight
                
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current
                    
        return self._visualize_paths(start, distances, previous)