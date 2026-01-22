
def football_match(N_players, M_tackles):
  from sys import setrecursionlimit
  setrecursionlimit(1 << 25)
  graph = [[] for i in range(N_players + 1)]

  for U_tackled, V in M_tackles:
    graph[U_tackled].append(V)
    graph[V].append(U_tackled)
  
  visited = [False] * (N_players + 1)
  color = [0]*(N_players+1)

  def DFS(U_tackled, C):
    visited[U_tackled] = True
    color[U_tackled] = C

    count =[0,0]
    count[0 if C==1 else -1]+=1

    for V in graph[U_tackled]:
      if not visited[V]:
        sub = DFS(V, -C)
        count[0] += sub[0]
        count[1] += sub[1]
      elif color[V] == color[U_tackled]:
        pass
    return count

  max_group = 0
  for i in range(1, N_players + 1):
    if not visited[i]:
      a,b = DFS(i,1)
      max_group += max(a,b)
  return max_group

N_players, M_tackles = map(int,input().split())
edges = []
for i in range(M_tackles):
  U_tackled, V = map(int, input().split())
  edges.append((U_tackled,V))


print(football_match(N_players, edges))