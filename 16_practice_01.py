# =====================================================================
# 종합 실습 1. 설비 종합 모니터링 리포트
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]
# (설비명, 온도, 진동)

# 판정 기준
#   온도 > 90 또는 진동 > 5.0  > "위험"
#   온도 >= 80 또는 진동 >= 3.0 > "주의"
#   그 외                      > "정상"

# TODO 1. 각 설비 상태 판정해서 번호 붙여 한 줄씩 출력 (for + enumerate + if/elif/else)

for na, mech in enumerate(sensors):
    tem = mech[1]
    jin = mech[2]
    if tem > 90 or jin > 5.0:
        print(f"{na} 상태:위험, 온도: {tem}, 진동: {jin}")
    elif tem >= 80 or jin >= 3.0:
        print(f"{na} 상태:주의, 온도: {tem}, 진동: {jin}")
    else:
        print(f"{na} 상태:정상, 온도: {tem}, 진동: {jin}")

# TODO 2. 정상 / 주의 / 위험 각각 몇 대인지 세서 출력 (누적변수)

normal = 0
dan = 0
danger = 0

for na, mech in enumerate(sensors):
    tem = mech[1]
    jin = mech[2]
    if tem > 90 or jin > 5.0:
        danger += 1
    elif tem >= 80 or jin >= 3.0:
        dan += 1
    else:
        normal += 1

print(f"정상: {normal}, 조심: {dan}, 위험: {danger}")

# TODO 3. 이상 설비(주의 + 위험) 비율 % 출력 (round)

rate = (dan + danger) / (normal + dan + danger) * 100
print(round(rate, 1), "%")

# TODO 4. 전체 평균 온도 출력 (round)
tt_temp = 0
for na, mech in enumerate(sensors):
    tem = mech[1]
    jin = mech[2]
    tt_temp += tem

print(round(tt_temp / len(sensors), 1))

# TODO 5. 온도 가장 높은 설비 이름 + 온도 출력 (반복문으로 직접 찾기)
na_mx = []
mx = 0
name = []
for na, mech in enumerate(sensors):
    name = mech[0]
    tem = mech[1]
    jin = mech[2]
    if tem > mx:
        mx = tem
        na_mx = name

print(f"온도 가장 높은 설비 이름: {na_mx}, 온도: {mx}")

# TODO 6. "위험" 설비 이름만 모아서 정렬해 리스트로 출력 (.append() + .sort())

danger_na = []
for na, mech in enumerate(sensors):
    tem = mech[1]
    jin = mech[2]
    if tem > 90 or jin > 5.0:
        danger_na.append(mech[0])

danger_na.sort()
print(f"위험 설비 목록: {danger_na}")


# 도전) 위험 1대라도 있으면 "⚠ 즉시 점검 요망", 없으면 "✅ 전 설비 안정"
