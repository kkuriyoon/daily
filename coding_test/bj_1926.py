import sys
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(y,x):
    q = [(y,x)]
    rs = 1
    while q:
        ey, ex = q.pop()
        for k in range(4):
            nx = ex + dx[k]
            ny = ey + dy[k]
            if 0<=nx<m and 0<=ny<n:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))

    return rs


cnt = 0
maxv = 0

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            cnt += 1
            chk[j][i] = True
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)