import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, target, adj, n):
    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()
        if node == target:
            break
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                q.append(neighbor)

    if not visited[target]:
        return -1, []
    path = []
    cur = target
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return len(path) - 1, path

N, M, S, D, K = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
if S == D == K:
    print(0)
    print(S)
    sys.exit()
dist1, path1 = bfs(S, K, adj, N)
if dist1 == -1:
    print(-1)
    sys.exit()
dist2, path2 = bfs(K, D, adj, N)
if dist2 == -1:
    print(-1)
    sys.exit()
full_path = path1 + path2[1:]
print(dist1 + dist2)
print(' '.join(map(str, full_path)))
