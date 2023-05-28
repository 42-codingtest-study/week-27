# 07강 _ N과 M (2)

n, m = map(int, input().split())
s = []

def dfs(start):

    if len(s) == m:
        for i in range(m):
            print(s[i], end = ' ')
        print('')
        return

    for i in range(start, n + 1):
        if i in s:
            continue
		
        s.append(i)
        dfs(i)
        s.pop()
dfs(1)