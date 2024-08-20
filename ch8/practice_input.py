import sys

print("Python", "Java",  sep = ",", end = "?")
# sep : 구분자 넣기
# end : 문장의 끝 부분을 ? 로 바꿔달라 
print("무엇이 더 재밌을까요?")

print("Python", "Java", file = sys.stdout) # 표준 출력
print("Python", "Java", file = sys.stderr) # 표준 오류 

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
  #print(subject, score)
  print(subject.ljust(8), str(score).rjust(4), sep = ":") 
  # ljust() 문자열을 왼쪽으로 정렬 / rjust() 문자열을 오른쪽으로 정렬 

# 은행 대기순번표 001, 002, 003, ...
for num in range(1, 21):
  print("대기번호 : " + str(num).zfill(3))
  # zfill() : 빈 칸 0으로 체우기

# 표준 입력
answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")
# 사용자 입력을 통해서 값을 받게 되면 항상 문자열 형태로 저장이 된다.
