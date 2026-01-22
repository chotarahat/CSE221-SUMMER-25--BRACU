from collections import deque

N, M, S, Q = map(int, input().split())

adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

sources = list(map(int, input().split()))
destinations = list(map(int, input().split()))

dist = [-1] * (N + 1)

queue = deque()
for src in sources:
    dist[src] = 0
    queue.append(src)

while queue:
    node = queue.popleft()
    for neighbor in adj[node]:
        if dist[neighbor] == -1:
            dist[neighbor] = dist[node] + 1
            queue.append(neighbor)

print(' '.join(str(dist[d] if dist[d] != -1 else -1) for d in destinations))