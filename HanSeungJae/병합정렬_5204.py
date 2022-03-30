from collections import deque
import sys
sys.stdin = open('input.txt')


def mergeSort(arr):
    if len(arr) == 1: return arr
    
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]
    
    left = mergeSort(left)
    right = mergeSort(right)
    
    return merge(left, right)


def merge(left, right):
    global cnt
    result = []
    left = deque(left)
    right = deque(right)
    
    if len(left) > 0 and len(right) > 0:
        if left[-1] > right[-1]:
            cnt += 1
    
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())
        elif len(left) > 0:
            result.append(left.popleft())
        elif len(right) > 0:
            result.append(right.popleft())
            
    return result
            

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    
    arr = mergeSort(arr)
    print(f'#{tc} {arr[n//2]} {cnt}')