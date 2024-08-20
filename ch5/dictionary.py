# 사전 key: value 가 한쌍
# key는 중복이 안됨

cabinet = {3: "유재석", 100: "조세호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# 만약 할당되지 않은 값을 출력한다면?
# []로 출력시 값을 가져올때 값이 없을경우 오류발생
# ()로 출력시 값이 없다면 None 출력하고 계속 이어나감
print(cabinet.get(5))
print(cabinet.get(5, "사용가능"))
print("ha")

print(3 in cabinet) # key in 변수
print(5 in cabinet)

cabinet = {"A-3": "유재석", "B-100": "조세호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "하하"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)