# 지역변수와 전역변수
gun = 10

def checkpoint(soldiers): # 경계근무
  #gun = 20
  global gun # 전역 공간에 있는 gun 사용
  gun = gun - soldiers
  print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
  gun = gun - soldiers
  print("[함수 내] 남은 총 : {0}".format(gun))
  return gun

print("전체 총 : {0}".format(gun))
#checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun,2)
print("남은 총 {0}".format(gun))

"""
1. 외부에서 gun 이라는 변수를 정의
2. checkpoint_ret() 함수를 호출하는데 외부에 있는 gun이라는 변수를 넘겨서 함수 내에서 계산
3. 변경된 값을 return 
4. return 된 값을 함수를 호출하는 곳에서 받음
"""