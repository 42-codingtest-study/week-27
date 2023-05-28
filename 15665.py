from itertools import combinations_with_replacement

N, M = map(int, input().split())
lst = [*map(int, input().split())]
lst.sort()

lst_set = set()
for i in combinations_with_replacement(lst, M):
    if i not in lst_set:
        lst_set.add(i)
        print(*i)
