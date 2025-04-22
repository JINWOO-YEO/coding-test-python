from collections import deque
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(input()))
visited = [[False]*M for _ in range(N)]
move = [[0,1],[1,0],[0,-1],[-1,0]]
bfs = deque()
bfs.append([0, 0, 1])
while not(bfs[0][0]==N-1 and bfs[0][1]==M-1):
    now = bfs.popleft()
    visited[now[0]][now[1]]=True
    for m in move:
        if now[0]+m[0]>=0 and now[0]+m[0] < N and now[1]+m[1]>=0 and now[1]+m[1] < M and graph[now[0]+m[0]][now[1]+m[1]]=='1' and visited[now[0]+m[0]][now[1]+m[1]]==False:
            bfs.append([now[0]+m[0],now[1]+m[1],now[2]+1])
print(bfs[0][2])