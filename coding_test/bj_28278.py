# 스택
# N은 명령의 수
# N개의 줄에 명령이 하나씩 주어짐

import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    ex = input().split()
    if ex[0] == '1':
        stack.append(ex[1])
    elif ex[0] == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif ex[0] == '3':
        count = len(stack)
        print(count)
    elif ex[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif ex[0] == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])