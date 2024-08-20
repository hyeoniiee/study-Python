"""
치킨 주문하기

다음 코드를 확인하고 예외처리 구문을 추가하시오.

조건1. 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리한다.
  출력문 : 값을 잘못 입력했습니다.
조건2. 대기 손님이 주문할 수 있는 최대 주문량은 10마리로 제한한다.
조건3. 치킨 소진 시 오류 SoldOutError를 발생시키고 프로그램을 종료한다.
  출력문 : 재료가 소진되어 더이상 주문을 받지 않습니다.
"""

class SoldOutError(Exception):
  pass

chicken = 10 # 남은 치킨 수
waiting = 1 # 대기 번호, 1부터 시작

while True:
  try:
    print("[남은 치킨 : {0}]".format(chicken))
    order = int(input("치킨을 몇 마리 주문하시겠습니까? "))
    if order > chicken: # 남은 치킨보다 주문량이 많을 때
      print("재료가 부족합니다.")
    elif order <= 0:
      raise ValueError
    else:
      print("[대기 번호 {0}] {1}마리를 주문했습니다.".format(waiting, order))
      waiting += 1 # 대기 번호 증가
      chicken -= order # 주문 수만큼 남은 치킨 감소
    if chicken == 0:
      raise SoldOutError
  except ValueError:
    print("잘못된 값을 입력했습니다.")
  except SoldOutError:
    print("재료가 소진되어 더 이상 주문을 받지 않습니다.")
    break
