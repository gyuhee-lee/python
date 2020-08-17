list_a = [273, 32, 103, "문자열", True, False]
print(list_a)
print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[1:3])
print()

# 요소 값 변경
list_a[0] = "변경"
print(list_a)
print()

# 음수를 넣어 뒤에서부터 요소 선택
print(list_a[-1])
print(list_a[-2])
print(list_a[-3])
print()

# 리스트 안의 문자열에서 특정 위치 값 출력
print(list_a[3])
print(list_a[3][0])
print(list_a[3][1])
print(list_a[3][2])
print()

# 리스트 안에 리스트 사용
list_b = [[1,2,3], [4,5,6], [7,8,9]]
print(list_b)
print(list_b[1])
print(list_b[1][1])

list_c = [1,2,3]
list_d = [4,5,6]
print("list_c = ", list_c)
print("list_d = ", list_d)
print("* 리스트 기본 연산자 :")
print("list_c + list_b = ", list_c + list_d)
print("list_c * 3 = ", list_c * 3)
print("* 길이 구하기 : ")
print("len(list_c) = ", len(list_c))