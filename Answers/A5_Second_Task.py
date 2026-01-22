import sys
sys.setrecursionlimit(2 * 100000 + 50)

n, m = map(int, input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))

adj = [[] for _ in range(n + 1)]
for u, v in zip(u_list, v_list):
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (n + 1)
result = []

def dfs(node):
    visited[node] = True
    result.append(node)
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor)
dfs(1)
print(' '.join(map(str, result)))
