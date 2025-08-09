# 수찾기, 복습

# 존재하면 1 존재하지 않으면 0

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
queries = list(map(int, input().split()))

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right :
        mid = (right + left) // 2
        if array[mid] == target :
            return 1
        elif array[mid] > target :
            right = mid - 1
        else :
            left = mid + 1
    return 0

for q in queries:
    print(binary_search(A,q))