from collections import deque
class Graph:
    def __init__(self):
        self.adj_list = {}

    def AddVertex(self, v):
        if v in self.adj_list:
            raise ValueError(f"Vertex {v} already exists in the graph.")
        self.adj_list[v] = []

    def AddEdge(self, u, v):
        if u not in self.adj_list:
            raise ValueError(f"Vertex {u} does not exist in the graph.")
        if v not in self.adj_list:
            raise ValueError(f"Vertex {v} does not exist in the graph.")
        if v in self.adj_list[u]:
            raise ValueError(f"Edge ({u}, {v}) already exists in the graph.")
        self.adj_list[u].append(v)

    def DeleteVertex(self, v):
        if v not in self.adj_list:
            raise ValueError(f"Vertex {v} does not exist in the graph.")
        del self.adj_list[v]
        for u in self.adj_list:
            if v in self.adj_list[u]:
                self.adj_list[u].remove(v)

    def DeleteEdge(self, u, v):
        if u not in self.adj_list:
            raise ValueError(f"Vertex {u} does not exist in the graph.")
        if v not in self.adj_list:
            raise ValueError(f"Vertex {v} does not exist in the graph.")
        if v not in self.adj_list[u]:
            raise ValueError(f"Edge ({u}, {v}) does not exist in the graph.")
        self.adj_list[u].remove(v)
        if u in self.adj_list[v]:  # Check if reverse edge exists
            self.adj_list[v].remove(u)

    def AdjMatrix(self):
        vertices = list(self.adj_list.keys())
        n = len(vertices)
        matrix = [[0] * n for _ in range(n)]
        for i, u in enumerate(vertices):
            for v in self.adj_list[u]:
                j = vertices.index(v)
                matrix[i][j] = 1
        return matrix
    
    def bfs(self, v):
        visited = []
        #deque will pop elements in O(1) time instead of O(n) with an array
        queue = deque()

        visited.append(v)
        queue.append(v)

        while queue:
            s = queue.popleft()
            print(s, end = " ")

            for n in self.adj_list[s]:
                if n not in visited:
                    visited.append(n)
                    queue.append(n)

    def dfs(self, v):
        visited = []
        stack = []
        
        visited.append(v)
        stack.append(v)

        while stack:
            s = stack.pop()
            print(s, end = " ")

            for n in reversed(self.adj_list[s]):
                if n not in visited:
                    visited.append(n)
                    stack.append(n)

        

# Create K5 graph
k5 = Graph()
for v in range(1, 6):
    k5.AddVertex(v)
for u in range(1, 5):
    for v in range(u + 1, 6):
        k5.AddEdge(u, v)

print("K5 graph:")
print(k5.adj_list)

# Convert K5 to K4 using DeleteVertex
k5.DeleteVertex(5)
print("K4 graph:")
print(k5.adj_list)

# Create K3,3 graph
k33 = Graph()
for v in range(1, 7):
    k33.AddVertex(v)
for u in range(1, 4):
    for v in range(4, 7):
        k33.AddEdge(u, v)

print("K3,3 graph:")
print(k33.adj_list)

# Convert K3,3 to C6
k33.DeleteEdge(1, 4)
k33.DeleteEdge(2, 5)
k33.DeleteEdge(3, 6)

# Add edges between consecutive vertices in each partition
k33.AddEdge(1, 2)
k33.AddEdge(2, 3)
k33.AddEdge(3, 1)
k33.AddEdge(4, 5)
k33.AddEdge(5, 6)
k33.AddEdge(6, 4)

print("C6 graph:")
print(k33.adj_list)


