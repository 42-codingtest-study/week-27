# 문제 이해 시간 제외 15분
import sys
input = sys.stdin.readline

d, k = map(int, input().split())
arr = list(map(int, input().split()))
geori_su = []
dung = k + (k-1) * d
# len() 시간복잡도 : O(1)
geori_len = len(arr) - dung + 1

for i in range (geori_len) :
    # list에서 인덱스 값 찾기 시간복잡도 : O(1)
    add = arr[i]
    for j in range (1, k):
        add = add * 10 + arr[i + (j * (d + 1))] 
    # append() 시간복잡도 : O(1)
    geori_su.append(add)

#print(geori_su)
# sort() 시간복잡도 : O(nlogn) -> 최악이네 다른 방법 ㄱ
geori_su.sort(reverse=True)
print(geori_su[0])