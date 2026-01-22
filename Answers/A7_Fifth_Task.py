import heapq

def parity_edges(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))

    dist = [[float('inf')] * 2 for _ in range(n + 1)]
    dist[1][0] = 0
    dist[1][1] = 0

    heap = [(0, 1, -1)] 

    while heap:
        cost, u, last_parity = heapq.heappop(heap)

        for v, w in graph[u]:
            curr_parity = w % 2
            if curr_parity == last_parity:
                continue 

            if dist[v][curr_parity] > cost + w:
                dist[v][curr_parity] = cost + w
                heapq.heappush(heap, (dist[v][curr_parity], v, curr_parity))

    res = min(dist[n][0], dist[n][1])
    print(-1 if res == float('inf') else res)

N, M = map(int, input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))
w_list = list(map(int, input().split()))

edges = []
for i in range(M):
    edges.append((u_list[i], v_list[i], w_list[i]))

parity_edges(N, edges)