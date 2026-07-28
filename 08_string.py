notice = """설비점검안내
1.전원확인
2.센서점검"""

print(notice)

# 삼중 따옴표를 사용할때, 맨 첫번째줄은 바로 뒤에 붙여줘야 1칸이 띄어지지않고 만들어짐

print("설비점검안내\n1.전원확인\n2.센서점검\n3.프린트를해보겠습니다")

backslash = "이름\\상태"
print(backslash)
# 첫번째\는 \가 문자로 들어간다는것을 알려주는 문자이다.


code = "PUMP_A"
state = "정상"
print(code, state, "2025-01-15", sep=" / ")

word = "PYTHON"
print(word[5] + "/" + word[4])


abc = "abcdefghijklnmopqrstuvwxyz"
# 자기 이름 출력하기
print(
    abc[2]
    + abc[7]
    + abc[14]
    + abc[9]
    + abc[5]
    + abc[14]
    + abc[5]
    + abc[12]
    + abc[6]
    + abc[8]
    + abc[25]
    + abc[25]
)


word = "PYTHON"
print(word[0:3] + "/" + word[3:6])

word = "temperature"
print(word[:4])  # temp

sensor = "temp_sensor"
print(sensor[0:])

word = "sensor_01"
print(word[-2::-1])  # 01

word = "PYTHON"
print(word[::2])

word = "PYTHON"
print(word[::-1])

# -----------------------------
phone = "01012345678"
print(len(phone))  # 11

# in - 특정 문자가 문자열에 포함되었는지 여부 확인
# "여부"를 확인하기 ㅇ때문에 True 또는 False (bool)으로 결과 반환
# 찾을 문자열 in 문자열
# .count()- 문자열에 특정 글자의 수(int)를 반환
# 문자열.count("찾을 글자")
# print("banana".count("a")) ##3
###banana를 ""를 써서 바로 씌워줘도 작용함
# print("010-1234-1234".count("-"))
# print("layla@spreatics.com.count("@")")
msg = "설비 고장 발생"
print("고장" in msg)
print("정상" in msg)

# print('고장' in '설비 고장 발생') ##True
# not in - in의 정반대 동작
# 따옴표로 감싼 공백(스페이스바)는 정말 "한 글자"로 취급한다.
text = "a,b,c,d"
print(text.count(","))  # 3

email = "choi@naver.com"
goalbang = email.find("@")
print(goalbang)  # 4
print(email[goalbang])
print("정상".find("고장"))

text = "a,b,c,d"
print(text.find(","))  # 3
print(text.find("e"))  # -1

fname = "sensor_log.csv"
print(fname.startswith("sensor"))  # True
print(fname.endswith(".csv"))  # True

alpha = "abc"
print(alpha == "abc")  # True
print(alpha == "ABC")  # True

# -------------------------------------------

str = "a,b,c,d,e,a,a"

print(str.count("a"))  # 3

print(str.count(","))  # 6

print(str.count(", "))  # 5 #count로 찾는 문자열과 완전히 동일해야 갯수를 샘

sqe = "SQE-00Q8"

sqe_index = sqe.find("SQE")
print(sqe_index)  # 0

sqe_index = sqe.find("-")
print(sqe_index)  # 3
sqe_fin = sqe[:sqe_index]  # sqe[0:3] > SQE
print(sqe_fin)  # SQE

# find 에서 했던 SQE 뽑아내기 실습 index 사용으로 바꾸기

sqe_index = sqe.find("-")
print(sqe_index)
sqe_fin = sqe[:sqe_index]
print(sqe_fin)

print("EQP-001".startswith("EQP"))

# 특정 문자열로 끝나는지 확인
# True / False로 반환

str2 = "월요일입니다! 여러분을 할 수 있어요!"

str2.endswith("!")  # True

fil = "sensor_log.csv"
print(fil.startswith("sensor"))  # True
print(fil.endswith(".csv"))  # True

# .으로 연결하는 이런 도구들은 메서드라고 부름
# 문자열이나 int, float처럼 특정 자료형 내부에 포함된 기능

# ========================

str3 = "abcdefg"
print(str3)
str = str3.upper()
print(str3)

str3 = str3.upper()

s = "ready"
big = s.upper()
print(big)  # READY


print("ABC".isupper())  # True
print("abc".islower())  # True
print("Abc".isupper())  # False

fname = "Sensor_LOG.CSV"
low = fname.lower()  # sensor_log.csv
print(low.startswith("sensor"))  # True
print(low.endswith(".csv"))  # True
print(fname.endswith(".csv"))  # False

pyh = "python"

print(pyh[:2] + pyh[2].upper() + pyh[3:])

# 공백 제거
# .strip():앞과 뒤의 모든공백 제거(중간 띄어쓰기는 그대로 유지됨)
# .lstrip():왼쪽 공백만 제거
# .rstrip():오른쪽 공백만 제거

raw = "          정상       "
print(raw.strip())  # 정상
print(raw.lstrip())  # 정상     "

# strip으로 가운데 공백은 제거 불가능

str4 = "===정상==="
print(str4.strip("="))  # 정상

# strip으로 특정 문자열을 지정하면 양옆에 있는 그 문자열을 지우게 함

raw = "   NORMAL   "
step1 = raw.strip()  # NORMAL
step2 = step1.lower()  # normal

chain = raw.strip().lower()  # normal

raw = raw.strip().lower()

print(raw.strip())


str = "      Warning   "

print(str.lower())
print(str.strip().lower())

s = "a,b,c,d"
print(s.split(","))  # ["a","b","c","d"]

s = "a,b,c,d"
print(s.split(","))  # ['a', 'b', 'c', 'd']

parts = ["2025", "01", "15"]
print("-".join(parts))  # 2025-01-15 (사이에 - 넣어 합침)

raw = "2025/01/15"
parts = raw.split("/")  # ['2025', '01', '15']
print("-".join(parts))  # 2025-01-15 (/ 를 - 로 교체)

raw = "1, NORMAL ,25.3"
parts = raw.split(",")  # ['1', ' NORMAL ', '25.3']
status = parts[1].strip().lower()
print(status)  # normal (공백 제거 후 소문자)

name = "PUMP_A"
temp = 87
print(f"설비 {name}, 온도 {temp}도")  # 설비 PUMP_A, 온도 87도


hour = 8

print(f"우리는 하루에 {hour}시간 수업을 듣고, 이는 {hour*60}시간 입니다.")

a = 1
b = 2
c = 3

print(f"평균:{int((a+b+c)/3)}입니다.")


rate = 87.456
print(f"{rate:.1f}")  # 87.5 (소수점 1자리, 반올림)
print(f"{rate:.2f}")  # 87.46 (소수점 2자리)

raw = " 5 , sensor_2 , WARNING , 0.78912 "
parts = raw.strip().split(",")  # 앞뒤 공백 제거 후 쉼표로 분리
sid = parts[1].strip()  # sensor_2
status = parts[2].strip().lower()  # warning
value = float(parts[3].strip())  # 0.78912
print(f"[센서 {sid}] 상태 {status}, 측정값 {value:.2f}")
