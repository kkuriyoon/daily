from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            home.append((r,c))
        elif city[r][c] == 2:
            chicken.append((r,c))
        
min_distance = float('inf')

for chicken_comb in combinations(chicken, M):
    total = 0
    for hx, hy in home:
        distance = min(abs(hx - cx) + abs(hy - cy) for cx, cy in chicken_comb)
        total += distance
    min_distance = min(min_distance, total)

print(min_distance)