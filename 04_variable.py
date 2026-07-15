# 변수 선언 방법
# 변수이름 = 값
# 오른쪽 값을 왼쪽 이름에 "저장"하라는 코드
temp = 36  # 숫자로 저장하고싶다면 따옴표 금지
name = "센서A"  # 문자는 무조건 따옴표로 감싸줘야함

print(temp)
print(name)

# =은 같다가 아니라 "저장"이라는 의미로 사용됩니다.
# =====================================

print("===== 변수 사용 활용 =====")  # print

x = 5
x = x + 5  # 변수를 재할당 할때 변수 기존의 자신의값을 활용할 수있음
y = 10
y = y + 5  # 오류발생. 왜냐하면 y가 선언되지 않았기 때문에.

# =====================================
print("====== 재할당 ======")

temp = 15  # 위에서 할당했던 36이라던 값을 15로 재할당(수정)
Temp = 15  # 위의 temp와 다른 변수로 동작함
print("temp:", temp)
print("Temp:", Temp)

# 재할당은 지금까지 실행된 코드 중 가장 마지막으로 저장된 값이 불려옴
score = 10
score = 20
score = 30
print(score)  # 30이 출력됨

print("===== 값 복사 =====")  # print

a = 10
b = a  # b 변수에는 10이 저장 (저장할 때의 그 순간의 a값을 b에 복사함)
print(b)  # 10이 출력됨

width, height = 10, 20  # width는 10, height는 20으로 저장됨
print("width:", width, "height:", height)

temp = 25
print(temp)
name = "센서A"
print(name)

temp = 30
temperature = temp
print(temperature)

my_number = 100
print(my_number)
mood = "happy"
print(mood)


age = 28
label = "28"
print(label)
print(age)

a = 100
b = a
a = 999
print(a)
print(b)

temp = 25
print(temp)  # 에러
score = 90
print(score)

temp = 25  # ℃
count = 3  # 센서 개수
# temp=100
print(temp)

x = 5
x = 10
x = x + 1
print(x)  # 11이 나올듯

temperature = "900℃"
name = "센서A"
press = 100
print(temperature)
print(name)
print(press)

# a=25, b=3 값을 알 수 없음
carburizing_a = 25
device_temperature = 3
print(carburizing_a)
print(device_temperature)

a, b, c = 10, 20, 30
print(a)
print(b)
print(c)
