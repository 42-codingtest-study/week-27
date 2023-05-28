wheel = [input().rstrip() for _ in range(4)]
K = int(input())

def dfs(n, d) :
    if n < 0 or n > 3 :
        return ;
    for i in [n - 1, n + 1] :
        if i >= 0 and i <= 3 :


for _ in range(K) :
    n, d = map(int, input().split())
