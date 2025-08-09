import sys
from collections import deque
input=sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

v1 = [False] * (N+1) # bfs
v2 = [False] * (N+1) # dfs

def bfs(V):
    q = deque([V])
    v1[V] = True
    while q:
        V = q.popleft()
        print(V, end = " ")
        for i in range(1, N+1):
            if v1[i] == False and graph[V][i]:
                q.append(i) 
                v1[i] = True

def dfs(V):
    v2[V] = True
    print(V, end = " ")
    for i in range(1, N+1):
        if v2[i] == False and graph[V][i]:
            dfs(i)

dfs(V)
print()
bfs(V)