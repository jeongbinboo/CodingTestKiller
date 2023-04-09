import sys
from collections import deque

my_input = sys.stdin.readline
next_node_list = deque()

n, m, k, x = [int(x) for x in my_input().split()]

root_list = [[] for _ in range(n + 1)]
min_root = [-1 for _ in range(n + 1)]
next_node_list.append(x)
min_root[x] = 0

for _ in range(m):
    a, b = [int(x) for x in my_input().split()]
    root_list[a].append(b)
for _ in range(k):
    for _ in range(len(next_node_list)):
        current_node = next_node_list.popleft()
        for next_node in root_list[current_node]:
            if min_root[next_node] == -1:
                next_node_list.append(next_node)
                min_root[next_node] = min_root[current_node] + 1
if k not in min_root:
    print(-1)
else:
    for i in range(1, n + 1):
        if min_root[i] == k:
            print(i)
