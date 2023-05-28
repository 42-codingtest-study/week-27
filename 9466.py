import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

t = int(input())

def dfs(i) :
    global cycle
    global ok
    if not visit[i] :
        visit[i] = True
        cycle.append(i)
        dfs(want[i])
    else :
        for k in range (len(cycle)) :
            if cycle[k] == i :
                ok += cycle[k:]
                continue

for _ in range (t):
    student = int(input())
    want = [0] + list(map(int, input().split()))
    visit = [True] + [False] * student 
    ok = []
    for i in range(1, student + 1):
        if not visit[i]:
            cycle = []
            dfs(i)
    print(student - len(ok))