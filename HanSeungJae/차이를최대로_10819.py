from itertools import permutations

def A_max(N, A):
    arrays = set(permutations(A, N))
    total_list = []

    for array in arrays:
        total = 0

        for idx in range(len(array)):
            if idx == len(array)-1:
                pass
            else:
                total += abs(array[idx] - array[idx+1])
        
        total_list.append(total)

    return max(total_list)

N = int(input())
A = map(int, input().split())

print(A_max(N, A))
