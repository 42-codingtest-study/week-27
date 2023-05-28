from collections import deque

N, K = map(int, input().split())


def bfs(v):
    dq = deque([v])
    d = [-1] * 100001
    d[v] = 0
    visited = [-1] * 100001

    while dq:
        v = dq.popleft()

        if v == K:
            path = [K]
            while visited[v] != -1:
                path.append(visited[v])
                v = visited[v]
            path.reverse()
            return d[K], path

        for i in (v - 1, v + 1, 2 * v):
            if 0 <= i <= 100000 and d[i] == -1:
                d[i] = d[v] + 1
                visited[i] = v
                dq.append(i)


distance, path = bfs(N)
print(distance)
print(" ".join(map(str, path)))
