import sys

sys.setrecursionlimit(10**7)


def dfs(curr, visited, finished):
    global cnt
    visited[curr] = True
    next_node = lst[curr]

    if visited[next_node]:
        if not finished[next_node]:
            while next_node != curr:
                cnt += 1
                next_node = lst[next_node]
            cnt += 1
    else:
        dfs(next_node, visited, finished)

    finished[curr] = True


for _ in range(int(input())):
    n = int(input())
    lst = [0] + list(map(int, input().split()))
    cnt = 0
    visited = [False] * (n + 1)
    finished = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, visited, finished)

    print(n - cnt)
