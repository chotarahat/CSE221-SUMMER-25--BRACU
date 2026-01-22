import heapq

def second_shortest_path(n, graph, source, dest):
    dist = [[float('inf')] * 2 for _ in range(n + 1)]
    dist[source][0] = 0

    heap = [(0, source)]

    while heap:
        cost, u = heapq.heappop(heap)

        for v, w in graph[u]:
            new_cost = cost + w

            if new_cost < dist[v][0]:
                dist[v][1] = dist[v][0]
                dist[v][0] = new_cost
                heapq.heappush(heap, (new_cost, v))

            elif dist[v][0] < new_cost < dist[v][1]:
                dist[v][1] = new_cost
                heapq.heappush(heap, (new_cost, v))

    result = dist[dest][1]
    print(-1 if result == float('inf') else result)

N, M, S, D = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

second_shortest_path(N, graph, S, D)