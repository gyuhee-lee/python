number = input("정수 입력 > ")
number = int(number)

# 양수 조건
if number > 0 :
    print("양수입니다.")
# 음수 조건
if number < 0 :
    print("음수입니다.")
# 0 조건
if number == 0 :
    print("0입니다.")
print()

# 끝자리로 짝수와 홀수 구분
number = input("정수 입력 > ")
# 마지막 자리 추출
last_number = number[-1]
last_number = int(last_number)
# 짝수확인
if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8 :
    print("짝수입니다.")
# 홀수확인
if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 6 \
    or last_number == 9 :
    print("홀수입니다.")
print()