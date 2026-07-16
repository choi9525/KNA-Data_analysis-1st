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
