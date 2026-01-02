class FordFulkerson:
    def __init__(self, graph):
        self.graph = graph  # 原始圖的殘留路徑矩陣
        self.ROW = len(graph)

    # 使用 DFS 尋找從源點 (s) 到匯點 (t) 的路徑
    def dfs(self, s, t, visited, path):
        visited[s] = True
        if s == t:
            return True
        
        for v, capacity in enumerate(self.graph[s]):
            # 如果還有剩餘容量且該點未訪問過
            if not visited[v] and capacity > 0:
                path[v] = s  # 紀錄路徑
                if self.dfs(v, t, visited, path):
                    return True
        return False

    def max_flow(self, source, sink):
        parent = [-1] * self.ROW
        max_f = 0

        # 當 DFS 仍能找到增廣路徑時，持續迭代
        while True:
            visited = [False] * self.ROW
            if not self.dfs(source, sink, visited, parent):
                break  # 找不到路徑了，跳出迴圈

            # 1. 找出這條路徑上的「瓶頸容量」（最小殘留流量）
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # 2. 更新殘留網路：正向邊減去流量，反向邊加上流量
            max_f += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow # 正向
                self.graph[v][u] += path_flow # 反向
                v = parent[v]

        return max_f

# 範例：鄰接矩陣表示
# graph[i][j] 代表從 i 到 j 的邊容量
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