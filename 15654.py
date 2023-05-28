# 07강 _ N과 M (5)

n, m = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
v = []

def dfs(depth) :
    if depth == m :
        print(' '.join(map(str, v)))
    else :
        for i in s :
            if i not in v :
                v.append(i)
                dfs(depth + 1)
                v.pop()
dfs(0)