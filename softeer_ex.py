# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())
graph = []
for _ in range (n):
	graph.append(list(map(int, input().split())))
	
def dfs(x,y):
	global area
	if x < 0 or y < 0 or x >= n or y >= n :
		return False
	if graph[x][y] == 1 :
		graph = 0
		area += 1
		dfs(x + 1, y)
		dfs(x, y + 1)
		dfs(x - 1, y)
		dfs(x, y - 1)
		return True
	return False

cnt = 0
areas = []
for i in range (n):
	for j in range (n):
		area = 0
		if dfs(i, j) :
			cnt += 1
			areas.append(area)
			
print(cnt)
areas.sort()
print(' '.join(map(str, areas)))
