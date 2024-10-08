# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")

for waiting_no in range(1, 5): # 순차적으로 숫자가 커질경우 range를 사용
  print("대기번호 : {0}".format(waiting_no))

star = ["아이언맨", "토르", "그루트"]
for customer in star:
  print("{0}, 커피가 준비되었습니다.".format(customer))

# 한 줄 for문
#출석번호가 1,2,3,4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student]
print(student)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)