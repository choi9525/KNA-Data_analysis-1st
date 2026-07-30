temp = [25, 26, 27, 28, 29, 31, 32, 33, 34]

for i in temp:
    if i > 30:
        print(f"위험, 고온:{i}")


for i in range(len(temp)):
    if i > 30:
        print("위험")

li = [4, 7, 6]

for i in range(len(li)):

    print(li[i])


temperature = [25, 35, 38, 26, 48, 24, 27, 46]
total = 0
count = 0

for i in temperature:
    if i > 30:
        print(f"이건 {i}℃이므로 고온입니다")
        total += i
        count += 1
print(f"고온의 합:{total}, 고온의 평균:{total/count}")


tp = [24, 25, 26, 28, 40, 41, 44, 67, 78]
rv = []

for f in tp:
    if f > 30:
        rv.append(f)

print(rv)


tps = [25, 27, 28, 29, 32, 43]
ferro = []

for t in tps:
    ferro.append(t * 1.8 + 32)

print(ferro)


temps = [15, 16, 25, 26, 27, 47, 48, 58]
total_value = 0
count = 0

total_value_nw = 0
nw = []

for i in temps:
    total_value += i
    count += 1
print(f"전체평균: {total_value/count}")


for k in temps:
    if k > 30:
        nw.append(k)
        total_value_nw += k
        count_nw = len(nw)

print(f"nw의 평균: {total_value_nw/count_nw}")
