customer = "토르"
index = 5
while index >= 1:
  print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
  index -= 1
  if index == 0:
    print("커피는 폐기처분 되었습니다.")

"""
customer1 = "아이언맨"
index = 1
while True: # 무한 루프
  print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer1, index))
  index += 1
"""

customer = "토르"
person = "Unknown"
while person != customer : # 조건이 만족할때까지 반복, 조건을 만족하면 반복문 탈출
  print("{0}, 커피가 준비 되었습니다.".format(customer))
  person = input("이름이 어떻게 되세요?")

absent = [2,5] #결석
no_book = [7] # 책 잊음
for student in range(1, 11):
  if student in absent:
    continue # 다음 반복을 진행
  elif student in no_book:
    print("오늘 수업 여기까지.")
    break # 바로 반복문 탈출
  print("{0}, 책을 읽어봐".format(student))