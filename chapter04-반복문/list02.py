list_a = [1,2,3]

print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

print("# 리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)
print()

print("# 리스트 연결 연산자와 요소 추가의 차이")
list_b = [4,5,6]
print("list_a + list_b = ", list_a + list_b)
print("list_a : ", list_a)
print("list_b : ", list_b)
print()
list_a.extend(list_b)
print("list_a : ", list_a)
print("list_b : ", list_b)
print()

print("# 리스트에서 요소 제거1")
del list_a[0]
print("del list_a[0] : ", list_a)
print("# 리스트에서 요소 제거2")
list_a.pop(3)
print("pop(3) : ", list_a)
print()

print("# 리스트 값으로 제거")
list_c = [1,2,1,2,3]
print("삭제 전 : ", list_c)
list_c.remove(2) # 리스트에 2가 두개, 앞에 한개만 제거
print("삭제 후 : ", list_c)
print()

print("# 리스트 모두 제거")
list_d = [5,6,7,8,8,9]
print("삭제 전 : ", list_d)
list_d.clear()
print("삭제 후 : ", list_d)
print()

print("# 리스트 내부에 값이 있는지 확인")
list_e = [273, 552, 13, 92]
print("list_e : ", list_e)
print("273 in list_e :", 273 in list_e)
print("99 in list_e :", 99 in list_e)
print("273 not in list_e :", 273 not in list_e)
print("99 not in list_e :", 99 not in list_e)