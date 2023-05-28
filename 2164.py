import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
card = deque([])

for i in range(n):
    card.append(i+1)
    # print(card)
    
while(1):
    if len(card) == 1:
        break
    else:
        card.popleft()
        temp = card.popleft()
        card.append(temp)
    
print(card.pop())