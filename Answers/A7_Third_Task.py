import heapq

def minimize_danger(n, graph):
    danger = []
    for _ in range(n + 1):
        danger.append(float('inf'))
    visited = [False] * (n + 1)

    danger[1] = 0
    heap = [(0, 1)]  

    while heap:
        curr_danger, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True

        for v, w in graph[u]:
            path_danger = max(curr_danger, w)
            if danger[v] > path_danger:
                danger[v] = path_danger
                heapq.heappush(heap, (danger[v], v))

    return danger


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w)) 

danger_levels = minimize_danger(N, graph)


for i in range(1, N + 1):
    if danger_levels[i] == float('inf'):
        print(-1, end=' ')
    else:
        print(danger_levels[i], end=' ')
print()