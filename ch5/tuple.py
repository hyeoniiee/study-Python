# 튜플은 리스트와 다르게 내용 변경이나 추가를 할 수 없다.
# 속도는 리스트보다 빨라 변경되지 않는 목록을 사영할 때 튜플을 활용할 수 있다.

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생성까스")

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)