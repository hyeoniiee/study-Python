"""
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst) # 값을 무작위로 섞음
print(lst)

Quiz) 당첨자 뽑기
댓글 작성자 중에서 추첨을 통해 1명은 치킨쿠폰, 3명은 커피쿠폰을 주려고 할때, 당첨자를 뽑는 추천 프로그램 작성하시오

조건1. 편의상 댓글은 20명, 아이디는 1 ~ 20 으로 가정
조건2. 무작위로 추첨하되 중복은 허용 안함
조건3. random 모듈과 shuffle() , sample() 함수 이용

출력문
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : 3, 6, 10
-- 축하합니다! --
"""
from random import *

user = range(1, 21)
print(type(user)) # <class 'range'>
user = list(user)
print(type(user)) # <class 'list'>
shuffle(user) # 값을 무작위로 섞음
print(user)

win = sample(user, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(win[0]))
print("커피 당첨자 : {0}".format(win[1:3]))
print("-- 축하합니다! --")

"""
셀프 체크
수강신청 기간에 일부 과목이 중복 신청되는 문제 발생. 중복 과목을 없애는 프로그램을 작성하시오.

조건1. 신청 과목은 리스트로 관리
조건2. 리스트에서 같은 과목이 2번 이상 포함된 경우 1개만 남기고 나머지는 삭제
조건3. 츨력 시 신청 과목의 순서는 변경해도 됨
"""

lst = ["자료구조", "알고리즘", "운영체제", "자료구조"]
print(lst, type(lst))
lst = set(lst)
print(lst, type(lst))
lst = list(lst)
print(lst, type(lst))
print("신청한 과목은 다음과 같습니다.")
print(lst)