# 사용자 입력 : input()
string = input("인사말을 입력하세요 > ")
print(string)
print(type(string))

string = input("입력 > ")
# print("입력 + 100", string+100) input()함수로 입력받은 자료는 모두 문자열로 저장되므로 문자열과 숫자는 더할 수 없어서 에러가 발생

# 문자열을 숫자로 바꾸기
stringA = input("입력 A : ")
intA = int(stringA)

stringB = input("입력 B : ")
intB = int(stringB)

print("문자열 자료 : ", stringA+stringB)
print("숫자 자료 : ", intA+intB)