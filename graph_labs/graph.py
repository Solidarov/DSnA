class UndirectedGraph:
    def __init__(self, *vertices):
        self.vertices = {v:i for i, v in enumerate(set(vertices))}
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
        

    def display_matrix(self):
        msg = '\n     ' + ' '.join(self.vertices.keys()) + "\n"
        for e, i in self.vertices.items():
            msg += f"{e} -> "
            for j in range(self.q_vertices):
                msg += f"{self.matrix[i][j]} "
            msg += "\n"
        return msg

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        result = [start]

        for neighbor in self.vertices:
        
            if self.matrix[self.vertices[start]][self.vertices[neighbor]] and neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        
        return result