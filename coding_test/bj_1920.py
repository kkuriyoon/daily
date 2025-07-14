# 이진탐색

N = int(input())
A = list(map(int, input().split()))

M = int(input())
queries = list(map(int, input().split()))

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right :
        mid = (left + right) // 2
        if array[mid] == target :
            return 1
        elif array[mid] < target :
            left = mid + 1
        else:
            right = mid - 1
    return 0

for q in queries :
    print(binary_search(A, q))