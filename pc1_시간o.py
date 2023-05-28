# 문제 이해 시간 제외 15분
import sys
input = sys.stdin.readline

d, k = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
dung = k + (k-1) * d
# len() 시간복잡도 : O(1)
geori_len = len(arr) - dung + 1

for i in range (geori_len) :
    # list에서 인덱스 값 찾기 시간복잡도 : O(1)
    add = arr[i]
    for j in range (1, k):
        add = add * 10 + arr[i + (j * (d + 1))] 
    # 배열에 거리수 다 넣지말고 그냥 젤 큰 값 기억하고 있기.
    if add > result :
        result = add

print(result)