from collections import deque
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
move = [[0,1],[1,0],[0,-1],[-1,0]]


def bfs(x, y):
    find = deque()
    find.append((x, y))
    while find:
        now = find.popleft()
        for m in move:
            dx = now[0]+m[0]
            dy = now[1]+m[1]
            if dx<0 or dx>=N or dy<0 or dy>=M:
                continue
            if graph[dx][dy]==1:
                find.append((dx,dy))
                graph[dx][dy]=graph[now[0]][now[1]]+1
    return graph[N-1][M-1]
print(bfs(0,0))