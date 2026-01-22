import heapq

def dijkstra(n, graph, source):
    dist = []
    for _ in range(n + 1):
        dist.append(float('inf'))

    dist[source] = 0
    heap = [(0, source)]

    while heap:
        d_u, u = heapq.heappop(heap)
        if d_u > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist


N, M, S, T = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


dist_S = dijkstra(N, graph, S)
dist_T = dijkstra(N, graph, T)

min_time = float('inf')
meeting_node = -1

for v in range(1, N + 1):
    if dist_S[v] != float('inf') and dist_T[v] != float('inf'):
        time = max(dist_S[v], dist_T[v])
        if time < min_time or (time == min_time and v < meeting_node):
            min_time = time
            meeting_node = v

if meeting_node == -1:
    print(-1)
else:
    print(min_time, meeting_node)