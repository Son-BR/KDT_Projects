# -----------------------------------------------------------------------
#  계산기 프로그램
# 필수조건 : 계산기 클래스

# 클래스명 : Calculator
# 속성/특징 : 필드 --> 색상, 제조자
# 역할/기능 : 함수/메서드 -->
#           - 계산기 인스턴스 생성메서드 ==> __init__()
#           - 계산기 속성/특징 값 읽기 ==> getter method
#           - 계산기 속성/특징 값 변경 ==> setter method
#           - 4칙연산 기능 메서드 => plus, minus, mul, div

# -----------------------------------------------------------------------

class Calculator:
    # 인스턴스 생성자
    def __init__(self,maker,color,*data):   # * -> 가변인자
        self.maker=maker
        self.color=color
        self.data=data

    # getter/method (선택)
    def getData(self): return self.data
    def setData(self,*data): self.data=data

    # 내가 원하는 계산기 기능
    def plus(self):
        count=0
        for i in range(len(self.data[0])):
            count+=int(self.data[0][i])
        print(f'plus => {count}')

    def minus(self):
        count=int(self.data[0][0])
        for i in range(1,len(self.data[0])):
            count=count-int(self.data[0][i])
        print(f'minus => {count}')

    def mul(self):
        count = int(self.data[0][0])
        for i in range(1, len(self.data[0])):
            count = count * int(self.data[0][i])
        print(f'mul => {count}')

    def div(self):
        count = int(self.data[0][0])
        for i in range(1, len(self.data[0])):
            count = count / int(self.data[0][i])
        print(f'mul => {count}')


    # 사용자 인터페이스(CUI) 기능 메서드
    def showUI(self):
        print('****** 계산기 ******')
        print('1. 덧셈')
        print('2. 뺄셈')
        print('3. 곱셈')
        print('4. 나눗셈')
        print('5. 종료')
        print('*******************')

# -----------------------------------------------------------------------

calcApp=Calculator('Sharp','Pink',None)

while True:
    calcApp.showUI()
    select=input('메뉴 선택')
    if select=='5': break


    elif select=='1':
        nums=input('숫자를 입력해 주세요.예)10,5').split(',')
        calcApp.setData(nums)
        calcApp.plus()

    elif select=='2':
        nums = input('숫자를 입력해 주세요.예)10,5').split(',')
        calcApp.setData(nums)
        calcApp.minus()

    elif select=='3':
        nums=input('숫자를 입력해 주세요.예)10,5').split(',')
        calcApp.setData(nums)
        calcApp.mul()

    elif select=='4':
        nums = input('숫자를 입력해 주세요.예)10,5').split(',')
        calcApp.setData(nums)
        calcApp.div()
