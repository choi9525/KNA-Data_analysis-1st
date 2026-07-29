# if 조건식:
# 실행할 코드 (한칸 들여쓰기)

temp = 85

if temp > 80:
    print("temp!")
    print("비상")
print("이건 항상 실행됨")


if temp > 80:
    print("경고")
else:
    print("정상")


age = int(input("나이를 입력하세요: "))
if age >= 19:
    print("성인입니다")
else:
    print("미성년자입니다")

    age = int(input("나이를 입력하시오"))
if age > 19:
    print("성인입니다")
else:
    print("미성년자입니다")

cor1 = 50
cor2 = int(input("정답을 입력하시오"))
if cor2 == cor1:
    print("정답입니다")
else:
    print("정답이 아닙니다")


age = int(input("나이를 입력하세요: "))
if age >= 19:
    print("성인입니다")
else:
    print("미성년자입니다")


input_color = input("신호등색을 입력하시오")
if input_color == "초록색":
    print("건너세요")
else:
    if input_color == "빨간색":
        print("기다리세요")
    else:
        print("다시입력하시오")


temp = int(input("온도를 입력하시오"))
if temp > 85:
    print("위험")
elif temp > 70:
    print("주의")
else:
    print("정상")


id = "id9525"
password = "9525"

input_id = int(input("아이디를 입력하시오"))
input_password = int(input("비밀번호를 입력하시오"))

if input_id == id and input_password == password:
    print("아이디가 일치합니다")
else:
    print("아이디가 일치하지않습니다.")


temp = int(input("온도: "))
vib = float(input("진동: "))
current = int(input("전류: "))
if temp > 80 or vib > 4.0:  # 1차: 하나라도 한계 초과면 즉시 위험
    print("위험: 즉시 정지")
else:  # 위험이 아닌 값만 2차 세부 판정
    if current > 60 and temp > 70:
        print("주의: 부하 점검")
    elif vib > 2.5:
        print("주의: 진동 관찰")
    else:
        print("정상")


# 반복문은 동일한 작업을 특정 횟수만큼 반복해야할 때
# 코드를 길게 쓰지 않고 반복시킬 수 있음

# for i in range(5)

n = int(input("얼마나 반복시킬래"))

for i in range(n):
    print("안녕하세요")


for i in range(1, 10, 2):
    print(i)

n = int(input("끝 숫자 N을 입력하세요: "))
for i in range(1, n + 1):  # 1부터 N까지
    print(i)
for i in range(2, n + 1, 2):  # 짝수만
    print(i)
for i in range(n, 0, -1):  # 역순
    print(i)


nc = int(input("범위를 입력하시오"))
for i in range(3, nc, 3):
    print(i)

nf = int(input("범위입력"))
for i in range(1, nf, 1):
    if i % 3 == 0:
        ab = i
        print(ab)

# 주의: nf가 아니라 nf+1을 해줘야 nf까지 계산됨


# list_len = int(len(list))
# for i in range(list_len):
# print(list[i])


for su in range(1, 10):
    print(f"2*{su}={2*su}")


# 1~5단 출력하기
# 필요한 변수:2개(몇단을 출력할건지)

for i in range(1, 6):
    for j in range(1, 10):
        print(f"{i}*{j}={i*j}")
