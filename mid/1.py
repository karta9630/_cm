# O(|f*|*|E|)  f* = max_flow
class FordFulkerson:
    def __init__(self, graph):
        self.graph = graph 
        self.ROW = len(graph)
    def dfs(self, s, t, visited, path):
        visited[s] = True
        if s == t:
            return True
        
        for v, capacity in enumerate(self.graph[s]):
            if not visited[v] and capacity > 0:
                path[v] = s  
                if self.dfs(v, t, visited, path):
                    return True
        return False

    def max_flow(self, source, sink):
        parent = [-1] * self.ROW
        max_f = 0
        while True:
            visited = [False] * self.ROW
            if not self.dfs(source, sink, visited, parent):
                break  
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_f += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow # 正
                self.graph[v][u] += path_flow # 反
                v = parent[v]

        return max_f

graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

ff = FordFulkerson(graph)
print(f"最大流為: {ff.max_flow(0, 5)}")