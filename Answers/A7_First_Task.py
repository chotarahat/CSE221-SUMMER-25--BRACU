import sys
import heapq


def dijkstra(n, graph, source, dest):
    dist = [float('inf')] * (n + 1)
    parent = [-1] * (n + 1)
    visited = [False] * (n + 1)

    dist[source] = 0
    heap = [(0, source)]

    while heap:
        d_u, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True

        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(heap, (dist[v], v))

    if dist[dest] == float('inf'):
        print(-1)
    else:
        print(dist[dest])
        path = []
        curr = dest
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        print(*path[::-1])

N, M, S, D = map(int, input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))
w_list = list(map(int, input().split()))


graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v, w = u_list[i], v_list[i], w_list[i]
    graph[u].append((v, w))

dijkstra(N, graph, S, D)