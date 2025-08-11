import sys

T = int(input())

for _ in range(T):
    str = sys.stdin.readline().rstrip()
    word = list(str.split())

    rv = []
    for i in word:
        rv.append(i[::-1])
    
    print(' '.join(rv))