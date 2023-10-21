from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

count_arr = defaultdict(int)

for num in arr:
    count_arr[num] += 1

stack = []

stack.append(arr[-1])
arr[-1] = -1

for i in range(N-2, -1, -1):
    flag = True
    while stack:
        if count_arr[arr[i]] < count_arr[stack[-1]]:
            temp = stack[-1]
            stack.append(arr[i])
            arr[i] = temp
            flag = False
            break
        else:
            stack.pop()
    if flag:
        stack.append(arr[i])
        arr[i] = -1
print(*arr)