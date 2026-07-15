print(3 + 5)
print(10 - 4)
print(4 * 5)
print(20 / 4)

print(7 // 3)  # 2
print(7 % 3)  # 1
print(2**5)  # 32


print(2 + 8 * 3)
print((2 + 8) * 3)

# +=:기존값에서 오른쪽값을 더한 뒤 재할당

result = 15
result += 10  # 25
print(result)
result -= 5  # 20
print(result)
result *= 3  # 60
print(result)
result /= 2  # 30
print(result)

# 문자열 연산
print("안녕" + "하세요")  # 안녕하세요
# 방법1:, 사용 방법2: 안녕뒤에 공백추가 방법3: 공백만 있는 문자열 더하기
print("안녕", "하세요")
print("안녕 하세요")
print("안녕", " ", "하세요")
