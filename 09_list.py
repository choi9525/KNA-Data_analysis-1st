# list는 python의 자료형 중 하나
# 여러개의 값을 [대괄호]에 감싸서 순대로 저장
# 나열된 값들은 자동으로 각자의 인덱스 번호를 순서대로 가지게 됨

temps = [35, 36, 37, 38]  # int 리스트
float_temps = [36.4, 36.5, 36.6, 36.7]  # float 리스트
machines = ["펌프", "압축기", "모터"]
mixed = ["펌프", 78, True]

print(temps[2])  # 37


temps = [35, 36, 34, 37, 36]
print(temps)  # [35, 36, 34, 37, 36]
print(len(temps))  # 5
empty = []
print(len(empty))  # 0

# 가장 첫번째 요소, 가장 마지막 요소
# -1을 사용하는 이유는 최신 갑승ㄴ 대체로 뒤에 추가가 됨
# 가자 최신 값은 결국 마지막 인덱스의 요소
# len 함수를 사용해서 리스트 길이-1로 계산이 가능하지만
# 이 작업이 번거로워 -1을 가장 많이 사용

temps = [22, 24, 27, 29, 26, 23]
print(temps[0])  # 22
print(temps[2])  # 27
print(temps[-1])  # 23


output = [120, 95, 130, 110, 88, 102]
first = output[0]
last = output[-1]
print(first + last)  # 222
print((first + last) / 2)  # 111.0


print(type(float_temps[0]))  # class "float"
print(type(machines[0]))  # class string


# 리스트 슬라이싱
# 리스트명[시작:끝:간격]
# 시작, 끝, 간격 인덱스는 모두 생략 가능 (문자열과 동일)

# print(temps[1:3]) #36, 37
# print(temps[:2])0


# 4
temps = [22, 24, 27, 29, 26, 23, 25, 28, 30, 21]
print(temps[:3])  # [22, 24, 27]
print(temps[-3:])  # [28, 30, 21]
print(len(temps[:3]))  # 3

# 5
hours = [3, 4, 5, 6, 5, 4, 6, 7, 8, 7, 5, 3]
first = hours[:6]
second = hours[6:]
print(first)  # [3, 4, 5, 6, 5, 4]
print(second)  # [6, 7, 8, 7, 5, 3]
print(len(first), len(second))  # 6 6


temps = [25, 26, 240, 28, 27]
print(240 in temps)  # True
i = temps.index(240)
temps[i] = 24
print(temps)  # [25, 26, 24, 28, 27]
print(240 in temps)  # False


nums = [1, 2, 3, 4, 5]

nums.append(999)
print(nums)  # [1,2,3,4,5,999]

# 만약 원본 리스트와 특정 값을 추가한 리스트 둘 다 필요하다면,
# 원본 리스트를 복사해서 리스트 수정 진행을 하면 됨


data = [1, 2, 3]
new_data = [7, 8, 9]

print(data.extend(new_data))  # [1,2,3,7,8,9]


temps = []
temps.append(30)
print(temps)  # [30]
temps.insert(0, 28)
print(temps)  # [28, 30]
temps.extend([31, 32])
print(temps)  # [28, 30, 31, 32]


list1 = ["딸기", "사과", "배", "포도", "수박", "망고"]
list1.remove("수박")
print(list1)


temps = [25, 26, 999, 24, 28, 26]
temps.remove(999)
print(temps)  # [25, 26, 24, 28, 26]
x = temps.pop(1)
print(x)  # 26
del temps[0]
print(temps)  # [24, 28, 26]


temps = [25, 26, 999, 24, 28, 26]
temps.remove(999)
print(temps)  # [25,26,24,28,26]
x = temps.pop(1)
print(x)  # 26
del temps[0]
print(temps)  # [24,28,26]

temps = []
temps.append(30)
print(temps)  # [30]
temps.extend([0, 28])
print(temps)  # [28,30]
temps.extend([31, 32])
print(temps)  # [28,30,31,32]

temps = [25, 26, 280, 27, 28]
print(280 in temps)  # True
i = temps.index(280)
temps[i] = 24
print(temps)  # [25,26,24,27,28]
print(240 in temps)  # False


hours = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first = hours[:4]  # 4
final = hours[4:]  # 5

temps = [24, 25, 26, 27, 28, 29]
first = temps[:3]
final = temps[-3:]
print(len(temps[:3]))  # 3


output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first = output[0]
final = output[-1]
print(first + final)  # 10


temps = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(temps[0])  # 1

temps = [0, 1, 2, 3, 4, 5]
print(len(temps))  # 6


temps = [1, 2, 3, 4, 5, 6, 7, 8, 9]
temps.sort()
print(temps)  # 동일
temps.reverse()
print(temps)  # 9,8,7,6,5,4,3,2,1


temps = [1, 2, 3, 4, 5, 6, 8, 999]
temps.remove(999)
print(temps)  # [1,2,3,4,5,6,7,8]
x = temps.pop(2)
print(x)  # 3
del temps[0]
print(temps)  # 2,4,5,6,7,8

temps = [1, 2, 3, 4, 5, 6, 7, 8, 9]
temps.append([30])
print(temps)  # [1,2,3,4,5,6,7,8,9,30]
temps.append([0, -1])
print(temps)  # [-1,1,2,3,4,5,6,7,8,9,30]
temps.extend([30])


temps = [25, 26, 240, 28, 27]
print(240 in temps)  # True
i = temps.index(240)
temps[i] = 24
print(temps)  # [25, 26, 24, 28, 27]
print(240 in temps)  # False

temps = [25, 26, 240, 28, 29]
print(240 in temps)
i = temps.index(240)
temps[i] = 24
print(temps)


hours = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first = hours[:4]
final = hours[4:]


n = [37, 2, 8, 109, 1004, -1, 22]
print("n리스트 원본:", n)

# 오름차순 정렬
n.sort()  # 원본 리스트 수정
print(n)  # [-1,2,8,22,37,109,1004]

# .count(찾을값)

# 특정 값의 위치 찾기
# .index(위치를 찾을 값)
# 리스트에서 가장 처 위치만 찾아줌
# print(f.index("일회용컵"))  # 1
# print(f)  # 원본 매열에 변화 없음
