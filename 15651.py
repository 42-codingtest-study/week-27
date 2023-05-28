# 07강 _ N과 M (3)

n, m = map(int, input().split())
s = []

def dfs(start) :
    if start == m :
        print(*s)
        return
    
    for i in range(n) :
        s.append(i + 1)
        dfs(start + 1)
        s.pop()
        
dfs(0)