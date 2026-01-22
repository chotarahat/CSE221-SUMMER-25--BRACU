# TASK A: Adjacency Matrix Representation

Node, Edge = (map(int,input().split()))

matrixx = []
for i in range(Node):
  matrixx.append([0] * Node)


for i in range(Edge):
  A,B,W = (map(int,input().split()))
  matrixx[A-1][B-1] = W

for i in range(len(matrixx)):
  for j in range(len(matrixx)):
    print(matrixx[i][j], end=" ")
  print()