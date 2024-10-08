class Unit:
  def __init__(self, name, hp, speed): # speed 추가
    self.name = name
    self.hp = hp
    self.speed = speed

  def move(self, location):
    print("[지상 유닛 이동]")
    print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): 
  def __init__(self, name, hp, speed, damage):
    Unit.__init__(self, name, hp, speed)
    self.damage = damage
  
  def attack(self, location):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
  
  def damaged(self, damage):
    print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
    self.hp -= damage
    print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
    if self.hp <= 0:
      print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
  def __init__(self, flying_speed):
    self.flying_speed = flying_speed

  def fly(self, name, location):
    print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
  def __init__(self, name, hp, damage, flying_speed):
    AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
    Flyable.__init__(self, flying_speed)
  
  def move(self, location): # Unit 클래스의 move() 메서드를 오버라이딩
    print("[공중 유닛 이동]")
    self.fly(self.name, location)

# 건물 유닛
class BuildingUnit(Unit):
  def __init__(self, name, hp, location):
    pass # 아무것도 안하고 일단은 넘어간다. (일단은 완성된것처럼 보임)
  # 함수뿐 아니라 if, for, while 등에서도 pass로 당장은 세부 동작을 정의하지 않고 나중에 다시 코드를 완성할 수 있다.

# 서플라잇 디폿 : 건물 유닛, 1개 건물 유닛 = 8유닛
supply_depot = BuildingUnit("서플라잇 디폿", 500, "7시") 

def game_start():
  print("[알림] 새로운 게임을 시작합니다.")

def game_over():
  pass

game_start()
game_over()