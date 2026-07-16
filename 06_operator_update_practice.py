print(3 + 5)
print(3 - 5)
print(3 * 5)
print(6 / 3)
print(3**2)  # 9
print(7 // 2)  # 3
print(7 % 2)  # 1


a = 10
b = 20
c = 30
print(a * b)  # 200
print(a * b * c)  # 6000

print("=== 비교연산자 ===")

# <(미만), >(초과), <=이하, >=이상, ==같다, !=다르다

print(7 < 16)  # True
print(7 == 7)  # True
print(7 != 4)  # True

# 비교연산자는 문자열 비교도 가능하다

# "안녕하세요" != "안녕하세요 "

# 논리연산자

# and / or / not -> 논리연산자

print(5 == 5 and 7 == 7)  # True + True = True

print(not True)  # False
# not : 값을 반대로 뒤집어줌
print(not 5 == 5)  # False

print(5 == 5)  # True
print(5 != 6)  # True
print(5 > 6)  # False
print(5 >= 6)  # False
print(5 <= 6)  # True


temperature = 85
temp_check = temperature >= 60 and temperature <= 90
pressure = 5
pressure_check = pressure >= 3 and pressure <= 7
print(temp_check, pressure_check)  # True True

stock = 100
stock += 50
print(stock)  # 150
stock -= 30
print(stock)  # 120
stock += 5
print(stock)  # 125

normal = 500
ex = 23
print(ex / normal * 100, "%")  # 23/5

real = 21
pr = 24
print(real / pr * 100, "%")  # 21/24

pa = 500
print(pa // 60, "시", pa % 60, "분")

name = input("이름: 정후")
print("안녕하세요,", name, "님!")
