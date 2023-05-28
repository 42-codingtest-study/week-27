# 07강 _ N과 M (4)

n, m = map(int, input().split())
s = []

def dfs(start, idx) :
    if start - 1 == m :
        print(''.join(map(str, s)))
        return
    for i in range(idx, n + 1) :
        s.append(i)
        dfs(start + 1, i)
        s.pop()
dfs(1, 1)