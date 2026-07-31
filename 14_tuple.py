sensor = ("모터온도", 78)  # 괄호 있고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = "모터온도", 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = (
    "모터온도",
    78,
)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'int'>

sensor = (78,)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>


tup = (1, "warning", 3)
print(tup.index("warning"))  # 2


# 튜플
# 리스트 안에 튜플을 담은 것을 표현

temps_13 = [("qox_001", 81), ("qox_002", 89), ("qox_003", 91), ("qox_004", 89)]

warning = 90

for name, temp in temps_13:
    if temp > 90:
        print(f"워링워링 온도가{temp}입니다.")


s1 = ("모터온도", 78)
print(s1)  # ('모터온도', 78)
print(s1[0])  # 모터온도
print(s1[1])  # 78
name, value = s1  # 언패킹
print(name, value)  # 모터온도 78


sensors = [
    ("모터온도", 78),
    ("회전속도", 1750),
    ("펌프압력", 95),
    ("유량", 42),
]


sensors = [
    ("모터온도", 78, (3, 5)),
    ("베어링진동", 0.5, (7, 2)),
    ("펌프압력", 95, (4, 8)),
]
for name, value, pos in sensors:
    x, y = pos
    print(name, "위치:", x, y)
for name, value, pos in sensors:
    x, y = pos
    if x <= 5:
        print(name, "1구역")  # 모터온도 / 펌프압력

sensor = ["모터온도", 78, (3, 5), ("베어링진동", 0.5, (7, 2))]
for name, value, pos in sensors:
    x, y = pos
    print(name, "위치:", x, y)
for name, value, pos in sensors:
    x, y = pos
    if x <= 5:
        print(name, "1구역")

sensors = [
    ("모터온도", 78, (3, 5)),
    ("베어링진동", 0.5, (7, 2)),
    ("펌프압력", 95, (4, 8)),
]
for name, value, pos in sensors:
    x, y = pos
    print(name, "위치:", x, y)
for name, value, pos in sensors:
    x, y = pos
    if x <= 5:
        print(name, "1구역")  # 모터온도 / 펌프압력

sensor = ["모터온도", 78, (3, 5), ("베어링진동", 0.5, (7, 2))]
for name, value, pos in sensors:
    x, y = pos
    print(name, "위치:", x, y)
for name, value, pos in sensors:
    x, y = pos
    if x <= 5:
        print(name, "1구역")
sensors = [
    ("모터온도", 78, (3, 5)),
    ("베어링진동", 0.5, (7, 2)),
    ("펌프압력", 95, (4, 8)),
]
for name, value, pos in sensors:
    x, y = pos
print(name, "위치:", x, y)
for name, value, pos in sensors:
    x, y = pos
if x <= 5:
    print(name, "1구역")  # 모터온도 / 펌프압력

    sensors = [
        ("모터온도", 78, (3, 5)),
        ("베어링진동", 0.5, (7, 2)),
        ("펌프압력", 95, (4, 8)),
    ]
for name, value, pos in sensors:
    x, y = pos
print(name, "위치:", x, y)
for name, value, pos in sensors:
    x, y = pos
if x <= 5:
    print(name, "1구역")  # 모터온도 / 펌프압력


logs = ["S01", "S02", "S01", "S03", "S02"]
unique = set(logs)
print(sorted(unique))  # ['S01', 'S02', 'S03']
print("종류 수:", len(unique))  # 종류 수: 3


line_a = {"S01", "S02", "S03", "S05"}
line_b = {"S03", "S04", "S05"}
print(line_a.union(line_b))  # 전체
print(line_a.intersection(line_b))  # {'S03', 'S05'}
print(line_a.difference(line_b))  # {'S01', 'S02'}
print(line_b.difference(line_a))  # {'S04'}


line_a = {"S01", "S02", "S03", "S05"}
line_b = {"S03,", "S04", "S05"}
print(line_a.union(line_b))


line_a = {"S01", "S02", "S03", "S05"}
line_b = {"S03", "S04", "S05"}
print(line_a.union(line_b))  # 전체
print(line_a.intersection(line_b))  # {'S03', 'S05'}
print(line_a.difference(line_b))  # {'S01', 'S02'}
print(line_b.difference(line_a))  # {'S04'}


yesterday = {"S01", "S02", "S03"}
today = {"S02", "S03", "S05"}
print(today.difference(yesterday))  # 신규: {'S05'}
print(today.intersection(yesterday))  # 지속: {'S02', 'S03'}

yesterday = {"S01", "S02", "S03"}
today = {"S02", "S03", "S05"}
print(today.difference(yesterday))  # 신규: {'S05'}
print(today.intersection(yesterday))  # 지속: {'S02', 'S03'}
