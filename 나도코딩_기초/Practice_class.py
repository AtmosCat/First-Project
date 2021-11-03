class Unit:
    def __init__(self):
        print("유닛 생성자")
    
class Flyable():
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() # FlyableUnit이 다중상속을 받았을 때 super를 사용하게 되는 경우 처음에 불러온 부모 클래스만 상속되므로 아래 줄처럼 따로따로 모든 부모 클래스들 써줘야 함
        Unit.__init__(self)
        Flyable.__init__(self)    

# 드랍쉽
dropship = FlyableUnit()   

