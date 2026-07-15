# int - 정수형

count = 3
age = 20
tall = 173

# 소수점 없이 딱 떨어지는 수

temp = -30
zero = 0

# float = 실수
# 소수점이 붙은 숫자

tried = 99.999
height = 17.2

# str - 문자열
# 따옴표에 감싸져있는 모든 값

hello = "안녕하세요~!"
empty = ""
illit = "It's me"

# bool - 불리언형
# True or False만
# 첫글자는 대문자, 따옴표 없이 작성

ok = True
no = False

print(100 < 5)  # False
print(100 > 5)  # True

# type(확인하고자 하는 것) > 입력한 것의 자료형을 알려줌

type(5)
print(type(5))
print(type("센서A"))
print(type(True))
print(type(3 > 2))

# 1.print 함수의 내부를확인
# 2. pring 함수에 또 함수가 있는것을 확인하고 typel 함수의 내부를 확인
# 3. type 함수의 내부에 연산자가 있는것을 확인하고 연산 진행
# 4. 3>2의 연산 결과는 TRUE이기 때문에 TYPE(TRUE)로 바뀜
# 5. TYPE(TRUE)의 결과인 <class 'bool>이 print로 인해 터미널에 출력

print(3, type(3))

num = 123
fake_num = "123"
str = "문자열"
ok = True

print(num, type(num))

print(num, ">>>", type(num))
print(num, ";", type(num))

print("=== 자료형마다 동작이 다른것 확인하기===")

print(3 + 5)
print("3" + "5")
print("안녕하" + "세요")

# 자주하는 실수

print(0.1 + 0.8)
print(round(0.1 + 0.8, 2))

print(10 / 2)
print(type(10 / 2))
