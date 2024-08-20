class Unit:
  def __init__(self):
    print("Unit 생성자")

class Flyable:
  def __init__(self):
    print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
  def __init__(self):
    super().__init__()
  # 2개 이상의 부모클래스를 다중상속 받을 때는 super를 쓰면 순서상 마지막에 상속받는 클래스에 대해서만 __init__함수 호출
  # 아런 문제가 있어 다중상속을 할때, 부모 클래스에대해 초기화가 필요하다하면 따로 명시적으로 
    Unit.__init__(self)
    Flyable.__init__(self)
  # 식으로 두번을 통해 초기화를 하는 방식을 사용할 수 있다.

# 드랍쉽
dropship = FlyableUnit()