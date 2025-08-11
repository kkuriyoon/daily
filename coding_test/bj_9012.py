import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    stack = []
    is_vps = True
    
    word = input().strip()
    for j in word:
        if j == '(':
            stack.append(j)
        else:
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
    
    if is_vps == True and len(stack) == 0:
        print("YES")
    else:
        print("NO")
