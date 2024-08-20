# finally : try 문에서 오류가 발생하든 안하든 try문을 벗어나는 시점에 무조건 실행되는 구문
# try - except 이루어진 구문의 가장 밑에 정의

class BigNumberError(Exception): # Exception 클래스 상속
  #pass
  def __init__(self, msg):
    self.msg = msg

  def __str__(self):
    return self.msg
    #return "[오류 코드 001] " + self.msg # 오류 메시지 가공

try:
  print("한 자리 숫자 나누기 전용 계산기입니다.")
  num1 = int(input("첫 번째 숫자를 입력하세요 : "))
  num2 = int(input("두 번째 숫자를 입력하세요 : "))
  if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
    # raise ValueError
    raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) 
  
  print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))

except ValueError:
  print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err: # 사용자 정의 예외 처리
  print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")
  print(err) # 오류 메시지 출력
finally: # 오류 발생 여부와 상관없이 항상 실행
  print("계산기를 이용해 주셔서 감사합니다.")