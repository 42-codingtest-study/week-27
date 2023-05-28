# 한시간 걸렸다 망할 시간복잡도는 ㄱㅊ을 것 같은데 공간이 좀 불안
import sys
input = sys.stdin.readline

# member = list(map(str, input().split()))
# period = list(map(int, input().split()))
# while True :
#     try:
#          pro_list = list(map(str, input()))
#          project.append(list(map(str, pro_list[i].split())))

member  = ["ro", "willi", "mor", "jer", "clyd"]
period  = [1, 1000, 1000, 1000, 100]
pro_list = ["willi mor clyd jer", "ro mor clyd", "willi jer", "mor", "clyd willi jer mor"]
project = []

# 정제
members = dict()
pm_cnt = dict()
for i in range (len(member)) :
    members[member[i]] = period[i]
    pm_cnt[member[i]] = 0
for i in range (len(pro_list)) :
    project.append(list(map(str, pro_list[i].split())))

def best_list(same_per, dic) :
    high = 0
    who = []
    for i in range(len(same_per)) :
        if high < dic[same_per[i]] :
            who = []
            high = dic[same_per[i]]
            who.append(same_per[i])
        elif high == dic[same_per[i]] :
            who.append(same_per[i])
        else :
            continue
    return  who

result = []
for i in range (len(project)) :
    best = []
    if member[0] in project[i] :
        result.append(member[0])
        pm_cnt[member[0]] += 1
        continue
    best = best_list(project[i], members)
    if len(best) == 1 :
        result.append(best[0])
        pm_cnt[best[0]] += 1
        continue
    best = best_list(best, pm_cnt)
    if len(best) != 1 :
        best.sort()
    result.append(best[0])
    pm_cnt[best[0]] += 1

print(result)

