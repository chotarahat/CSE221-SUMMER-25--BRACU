from collections import deque

def bfs(start,graph, n):
  visited = [False] * (n+1)
  distance = [0] * (n+1)

  queue = deque([start])
  visited[start] = True

  farthest_node = start

  while queue:
    u = queue.popleft()
    for v in graph[u]:
      if not visited[v]:
        visited[v]= True
        distance[v] = distance[u] + 1
        queue.append(v)
        if distance[v]>distance[farthest_node]:
          farthest_node = v
  return farthest_node, distance[farthest_node]  
def find_diameter(n, edges):
  graph = [[] for i in range(n+1)]
  for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)

  A,B = bfs(1,graph,n)
  C,diameter = bfs(A,graph,n)

  return diameter, A, C

n = int(input())
edges = [tuple(map(int, input().split())) for i in range(n-1)]
length,A,C = find_diameter(n,edges)
print(length)
print(A,C)