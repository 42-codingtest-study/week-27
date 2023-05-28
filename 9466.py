import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(x):
    global res
    visited[x] = True
    cycle.append(x) #사이클을 이루는 팀을 확인하기 위함
    num = lst[x]
    # print("idx", i, "outcycle :", cycle)
    
    if visited[num] == True: #방문가능한 곳이 끝났는지
        if num in cycle:  #사이클 가능 여부
            res +=cycle[cycle.index(num):]
            # print("idx", i, "cycle :", cycle,cycle[cycle.index(num):])
            # print(res)
            return
    else:
        dfs(num)

t = int(input())
for _ in range(t):
    n = int(input())
    lst = []
    lst = [0] + list(map(int, input().split()))
    visited = [True] + [False] * n
    # print(arr)
    res = []

    for i in range(1, n + 1):
        if visited[i] == False:
            # print("visited[i]" , i, visited[i])
            cycle = []
            # print("main cycle", cycle)
            dfs(i)
    # res = set(res)
    print(n - len(res))




