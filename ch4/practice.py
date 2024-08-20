#문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

#슬라이싱 slicing : 원하는 만큼 데이터를 자를 수 있음
jumin = "990101-1234567"
print("성별 : " + jumin[7]) 
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0 , 1)
print("월 : " + jumin[2:4]) 
print("일 : " + jumin[4:6]) 

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 -> jumin[0:6]과 같음
print("주민번호 뒷자리 : " + jumin[7:]) # 7 부터 끝까지 -> jumin[7:14]와 같음

# 뒤에서 슬라이싱 할려면 음수 인덱스를 사용
# 양수 인덱스는 0부터 시작이지만 음수 인덱스는 -1부터 시작
print("주민번호 뒷자리(뒤에서부터) : " + jumin[-7:]) # 뒤에서 7번째 위치부터 끝까지

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 문자열을 소문자로 변환
print(python.upper()) # 문자열을 대문자로 변환 
print(python[0].isupper()) # 인덱스 0에 있는 값의 문자열이 대문자인지 확인
print(len(python)) # 전체 문자열의 길이 반환 (공백 포함)
print(python.replace("Python", "Java")) # Python 를 찾아 Java 로 변경

index = python.index("n") # 문자열에서 처음 발견하는 n 의 인덱스 위치
print(index) #5
index = python.index("n", index + 1) # 두번째로 발견하는 n 의 인덱스 위치
print(index) #15

# find에서 원하는 값이 없으면 -1을 반환, index에서 원하는 값이 없으면 오류 발생 
print(python.find("Java")) # 내가 원하는 값이 변수에 포함되어 있지 않으면 -1 을 반환
#print(python.index("Java")) # 오류 발생

print(python.count("n")) # 지정한 문자나 문자열이 총 몇번 나오는지 횟수 확인