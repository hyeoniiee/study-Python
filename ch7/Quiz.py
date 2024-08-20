"""
표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중
(성별에 따른 공식)
남자 : 키(m) * 키(m) * 22
여자 : 키(m) * 키(m) * 21

조건1. 표준 체중은 별도의 함수 내에서 계산
  * 함수명 : std_weight
  * 전달값 : 키(hright), 성별(gender)
조건2. 표준 체중은 소수점 둘째자리까지 표시

출력문)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
"""
def std_weight(height, gender): # 키 m 단위 (실수), "남자" / "여자"
  if gender == "남자":
    return height * height * 22
  else:
    return height * height * 21
  
height = 175 # cm단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

"""
셀프체크
미세먼지 수치를 입력받아 대기질 상태를 출력하는 함수 만들기

조건1. get_air_quality 라는 이름의 함수 생성
조건2. 이 함수는 전달값으로 미세먼지 수치 입력 받음
조건3. 이 함수는 대기질 상태를 반환
조건4. 미세먼지 수치에 따른 대기질 상태
  좋음 : 0 ~ 30
  보통 : 31 ~ 80
  나쁨 : 81 ~ 150
  매우 나쁨 : 151 이상
조건5. 함수에 전달되는 전달값은 항상 0 이상의 값이라고 가정
"""
def get_air_quality(dust):
  if 0 <= dust <= 30:
    return "좋음"
  elif 31 <= dust <= 80:
    return "보통"
  elif 81 <= dust <= 150:
    return "나쁨"
  else: 
    return "매우 나쁨"
  
print(get_air_quality(20))
print(get_air_quality(55))