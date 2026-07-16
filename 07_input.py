name = input("이름: ")
print("안녕하세요,", name, "님!")

print("출력")
print(5)
# 어쨋든 터미널에서 보이는 출력된 값은 "글자와"같이 봉미
# input을 사용해서 값을 받는 곳도 터미널
# input을 통해 사용자에게 값을 입력받는 경우는 무조건 "str" 타입이 된다.

name = input("이름: ")
print("어서오세요", name, "님")

# input으로 받은 값은 변수에 저장하지 않으면 휘발됨
# 땜에 변수에 저장하는것이 추천됨

# input으로 받은값은 무조건 str으로
# 저장됨

year = int(input("태어난 연도: "))
print("당신의 현재 나이는", 2026 - year + 1, "세 입니다")

# float() 실수로 작성된 문자열을 float으로 변환해줌

print(float(12))  # 12.0

year = int(input("당신이 태어난 연도를 말하시오"))
print("당신이 나이는" + str(2026 - year + 1) + "입니다")


#! 중요:input을 사용하면 무조건 str을 받게 됨

nt = input("거주국가를 입력하시오")
city = input("도시를 입력하시오")

print("거주국가: " + nt + "의" + city + "에 거주함")

any = int(input("아무거나 입력하시오"))
thing = int(input("더 큰 아무거나 입력하시오"))
print("덧셈은" + str(any + thing) + "입니다")
print("뺄셈은" + str(any - thing) + "입니다")

temperature = int(input("온도를 입력하시오"))
print("80을 초과하였습니다.", 80 < temperature)

print("0이상입니다", "temperature>=0")

a = int(input("입력"))
b = int(input("입력"))
c = int(input("입력"))

avg = (a + b + c) / 3

print("50을 초과하였습니다.", avg > 50)
