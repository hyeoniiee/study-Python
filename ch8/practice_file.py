score_file = open("score.txt", "w", encoding="utf8") # 파일 내용 쓰기
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close

score_file = open("score.txt", "a", encoding="utf8") # 파일 내용 이어쓰기
score_file.write("과학 : 80") # 줄 바꿈이 없어서 설정해야 함
score_file.write("\n코딩 : 100")
score_file.close

score_file = open("score.txt", "r", encoding="utf8") # 파일 내용 읽기
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") 
print(score_file.readline()) # 줄 별로 읽기, 한줄 읽고 커서는 다음줄로 이동
print(score_file.readline())
print(score_file.readline(), end="") # 줄 바꿈을 안하고 싶다면 end 사용
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") 
while True: # 타입이 몇줄인지 모를때 반복문을 통해 파일 내용을 불러올 수 있다. 
  line = score_file.readline()
  if not line:
    break
  print(line) # 만약 줄바꿈을 안한다면 end 사용
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") 
lines = score_file.readline() # list 형태로 저장
for line in lines:
  print(line, end="")
score_file.close()
