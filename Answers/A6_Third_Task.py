from collections import deque

def knight_moves():
    N = int(input())
    x1, y1, x2, y2 = map(int, input().split())

    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

  
    directions = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]


    visited = [[False] * N for _ in range(N)]
    queue = deque([(x1, y1, 0)]) 
    visited[x1][y1] = True

    while queue:
        x, y, moves = queue.popleft()
        if x == x2 and y == y2:
            print(moves)
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))

    print(-1)

knight_moves()


