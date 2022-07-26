# --------------------------------------------------------------------
# 상속(Inheritance) -> 기존 클래스의 모든 것을 가져다가 사용하는 것 => 재사용
# 표현 : class 클래스명(기존클래스명):
# --------------------------------------------------------------------

class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def displayInfo(self):
        print(f'A => {self.x}, {self.y}')

class B(A):
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y
    #
    # def displayInfo(self):
    #     print(f'A => {self.x}, {self.y}')

    def calc(self):
        print(self.x * self.y)

b=B(5,3)
b.displayInfo()
b.calc()

class C(B):
    def add(self):
        print(self.x + self.y)

    # 오버라이딩(Overriding) - 상속받은 메소드에 한정, 함수구현부분 재정의
    def calc(self):
        print(self.x * self.y,self.x / self.y,self.x + self.y,self.x - self.y)

c=C(12,5)
c.displayInfo()
c.calc()

print(19*21*28)