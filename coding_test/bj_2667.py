# dfs 재귀
# each rs

N = int(input())
map = [list(map(int, input().strip()))for _ in range(N)]
chk = [[False] * N for _ in range(N)]

each = 0
rs = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(y,x):
    global each
    each += 1   
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=nx<N and 0<=ny<N:
            if chk[ny][nx] == False and map[ny][nx] == 1:
                chk[ny][nx] = True
                dfs(ny, nx)


for j in range(N):
    for i in range(N):
        if chk[j][i] == False and map[j][i] == 1:
            each = 0
            chk[j][i] = True
            dfs(j,i)
            rs.append(each)

rs.sort()
print(len(rs))
for i in rs:
    print(i)