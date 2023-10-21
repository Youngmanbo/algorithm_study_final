from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

count_arr = defaultdict(int)

for num in arr:
    count_arr[num] += 1

stack = []
other_stack = []

stack.append(arr[-1])
arr[-1] = -1