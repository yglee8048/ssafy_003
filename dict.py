"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}
scores = list(iu_score.values())
tot = sum(scores)
avg = tot / len(iu_score)
print(avg)



# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}

scores = list(score.values())
cnt = 0
tot = 0
for x in scores:
    tot = tot + sum(list(x.values()))
    cnt += len(x)

print(tot / cnt)



city = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

# 3. 도시별 최근 3일의 온도 평균은?
for x in city:
    tot = sum(city[x])
    avg = tot / len(city[x])
    print("{0} : {1:.2f}".format(x, avg))
    # round : 반올림

# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
largest = -987654321
smallest = 987654321
min_city = ""
max_city = ""
for x in city:
    local_max = max(city[x])
    local_min = min(city[x])
    if largest < local_max :
        largest = local_max
        max_city = x
    if smallest > local_min :
        smallest = local_min
        min_city = x
    
print("가장 추웠던 곳은 {0}. 가장 더웠던 곳은 {1}".format(min_city, max_city))

# 4. 위에서 서울은 영상 2도였던 적이 있나요?
ck = False
for x in city["서울"]:
    if(x >= 2):
        ck = True
        break

if(ck) : print("YES")
else : print("NO")