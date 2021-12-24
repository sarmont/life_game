n = 5
visited = [False] * (n + 1)
prev = [None] * (n + 1)
def dfs(start, visited, prev, g):
    visited[start] = True
    for u in g[start]:
        if not visited[u]:
            prev[u] = start 
            dfs(u)
dfs(0, visited, prev, g)