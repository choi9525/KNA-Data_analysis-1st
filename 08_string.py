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
