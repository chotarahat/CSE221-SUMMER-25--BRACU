def bfs(graph, start):
    colour = {}
    for unvisited in graph:
        colour[unvisited] = 0
    queue = []
    front = 0
    colour[start] = 1
    queue.append(start)
    traversal = []

    while front < len(queue):
        u = queue[front]
        front += 1
        traversal.append(u)

        for v in graph[u]:
            if colour[v] == 0:
                colour[v] = 1
                queue.append(v)

    return traversal

n, m = map(int, input().split())
graph = {}
for i in range(1, n + 1):
    graph[i] = []

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for u in graph:
    neighbors = graph[u]

    n = len(neighbors)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if neighbors[j] < neighbors[min_idx]:
                min_idx = j
    
        neighbors[i], neighbors[min_idx] = neighbors[min_idx], neighbors[i]
    
    graph[u] = neighbors


result = bfs(graph, 1)
print(" ".join(map(str, result)))