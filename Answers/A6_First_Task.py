def topological_sort(n, edges):
  adj = [[] for i in range(N_courses + 1)]
  in_degree = [0] * (N_courses + 1)

  for A, B in edges:
    adj[A].append(B)
    in_degree[B] += 1

  queue = []
  for i in range(1, N_courses+1):
    if in_degree[i] == 0:
      queue.append(i)

  order = []
  front = 0
  while front< len(queue):
    node = queue[front]
    front +=1 
    order.append(node)

    for neighbor in adj[node]:
      in_degree[neighbor] -=1
      if in_degree[neighbor] == 0:
        queue.append(neighbor)
        
  if len(order) != N_courses:
    return [-1]
  return order

N_courses, M_req = map(int, input().split())
edges =[]
for i in range(M_req):
    A, B = map(int, input().split())
    edges.append((A,B))

result = topological_sort(N_courses, edges)
print(' '.join(map(str, result)))