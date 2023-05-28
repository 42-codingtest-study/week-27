from itertools import permutations

N, M = map(int, input().split())
lst = [*map(int, input().split())]
lst.sort()

lst_set = set()
for i in permutations(lst, M):
    if i not in lst_set:
        lst_set.add(i)
        print(*i)
