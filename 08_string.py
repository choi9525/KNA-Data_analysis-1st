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
print(word[-2:])  # 01

word = "PYTHON"
print(word[::2])

word = "PYTHON"
print(word[::-1])
