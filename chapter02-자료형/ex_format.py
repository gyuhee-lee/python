# format : 문자열이 가지고 있는 함수

# "{}".format(10)
# "{} {}".format(10, 20)
# "{} {} {} {} {}".format(101, 202, 303, 404, 505)

string_a = "{}".format(10)
print(string_a)
print(type(string_a))

format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)
print(format_a)
print(format_b)
print(format_c)
print(format_d)

# "{} {}".format(1, 2, 3, 4, 5) -> 매개변수가 {} 보다 많은 경우 {} 개수만큼 적용되고 나머지는 버려짐
# "{} {} {}"format(1, 2) -> {}가 매개변수보다 많은 경우 Index Error라는 예외가 발생함

# 숫자 관련해서도 굉장히 다양한 기능을 가지고 있음
# 정수
output_a = "{:d}".format(52)
print(output_a)

# 특정 칸에 출력하기
output_b = "{:5d}".format(52) # 52앞에 공백 5칸
output_c = "{:10d}".format(52) # 52앞에 공백 10칸
print(output_b)
print(output_c)

# 빈 칸을 0으로 채우기
output_d = "{:05d}".format(52) # 양수
output_e = "{:05d}".format(-52) # 음수
print(output_d)
print(output_e)

# 양수, 음수 기호와 함께 출력하기
output_f = "{:+d}".format(52)
output_g = "{:-d}".format(-52)
print(output_f)
print(output_g)
output_h = "{: d}".format(52)
output_i = "{: d}".format(-52)
print(output_h)
print(output_i)
# 음수는 기호 표기 여부와 상관없이 보여주고, 양수는 + 표기를 해주어야 양수 기호를 보여줌

# 기호 조합하기
# 기호 뒤로 밀기
output_j = "{:+5d}".format(52)
print(output_j)
# 기호 앞으로 밀기
output_k = "{:=+5d}".format(52)
print(output_k)

# 부동 소수점 다양한 출력
output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)
output_c = "{:+15f}".format(52.273)
output_d = "{:+015f}".format(52.273)
print(output_a)
print(output_b)
print(output_c)
print(output_d)

output_a = "{:15.3f}".format(52.273)
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format(52.273)
print(output_a)
print(output_b)
print(output_c)

output_a = "{:.3f}".format(52.273)
output_b = "{:.2f}".format(52.273)
output_c = "{:.1f}".format(52.273)
print(output_a)
print(output_b)
print(output_c)

# 의미 없는 소수점 제거하기
output_a = 52.0
output_b = "{:g}".format(output_a)
print(output_a)
print(output_b)