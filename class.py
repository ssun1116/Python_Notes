# 클래스
name = "마린"
hp = 40
damage = 5

print("{0} 유닛이 생성되었습니다." .format(name))
print("체력 {0}, 공격력 {1}\n" .format(hp, damage))

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다." .format(tank_name))
print("체력 {0}, 공격력 {1}\n" .format(tank_hp, tank_damage))

## 매번 이 값을 입력해주기 어렵다... 클래스 = 붕어빵 틀 기계. 

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" .format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

## 클래스로 붕어빵 틀 만들기.
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다." .format(self.name))
        print("체력 {0}, 공격력 {1}" .format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# __init__ : 객체가 만들어질 때 기본적으로 init에 정의된 갯수와 동일하게 값이 들어가야 함.
# 이름만 넘기거나, 더 많은 정보를 넘기는 것은 불가능.

# 멤버변수
## 클래스 내에서 정의된 변수. name, hp, damage.
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}" .format(wraith1.name, wraith1.damage)) # .: 약간 R에서 $랑 비슷한 느낌

wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True
if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다." .format(wraith2.name))

## 클로킹 변수 : 외부에서 추가로 할당한 것. 클래스 내에서는 없다.
## 객체에 추가로 변수 외부에서 만들어 쓰기가 가능. 변수 확장 -> 확장한 개체에만 적용됨.

# 메소드
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다." .format(self.name))
        print("체력 {0}, 공격력 {1}" .format(self.hp, self.damage))

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. 공격력 {2}" .format(self.name, location, self.damage))
    # self : 클래스 내에서 메소드 쓸 때는 늘 self를 맨 앞에 쓴다.
   
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다." .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다." .format(self.name))

filebat1 = AttackUnit("파이어뱃", 50, 16)
filebat1.attack("5시")
filebat1.damaged(25)
filebat1.damaged(25)

# 상속 : 클래스끼리 물려주는 것.
class Unit: # 부모 클래스
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit): # 자식 클래스
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # Unit에서 self의 name, hp을 전달받음.
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. 공격력 {2}" .format(self.name, location, self.damage))
    # self : 클래스 내에서 메소드 쓸 때는 늘 self를 맨 앞에 쓴다.
   
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다." .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다." .format(self.name))
 
filebat1 = AttackUnit("파이어뱃", 50, 16)
filebat1.attack("5시")
filebat1.damaged(25)
filebat1.damaged(25)

# 다중상속 : 부모 클래스가 둘 이상.
class Unit: # 부모 클래스
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit): # 자식 클래스
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # Unit에서 self의 name, hp을 전달받음.
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. 공격력 {2}" .format(self.name, location, self.damage))
    # self : 클래스 내에서 메소드 쓸 때는 늘 self를 맨 앞에 쓴다.
   
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다." .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다." .format(self.name))
 
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

