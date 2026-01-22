import heapq

def beautiful_path(n, graph, weights, source, dest):
    cost = []
    for _ in range(n + 1):
        cost.append(float('inf'))
    visited = [False] * (n + 1)

    cost[source] = weights[source]
    heap = [(cost[source], source)]

    while heap:
        curr_cost, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True

        for v in graph[u]:
            path_cost = curr_cost + weights[v]
            if cost[v] > path_cost:
                cost[v] = path_cost
                heapq.heappush(heap, (cost[v], v))

    if cost[dest] == float('inf'):
        print(-1)
    else:
        print(cost[dest])

N, M, S, D = map(int, input().split())
w_list = list(map(int, input().split()))
weights = [0] + w_list  # 1-indexed

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    
beautiful_path(N, graph, weights, S, D)