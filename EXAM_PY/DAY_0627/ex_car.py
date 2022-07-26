#--------------------------------------------------------
# 현대 자동차를 표현하는 데이터 타입 즉 class 생성
# 클래스명 : car
# 속성/특징 : 제조사, 차번호, 차종류, 색상
#           -> 클래스 변수 :
#           -> 인스턴스 변수 :
# 역학/기능 : 이동한다, 정지한다, 차정보 출력한다
#           -> 이동한다 => 000자동차가 xx에서 xx로 간다.
#           -> 정지한다 => 000자동차가 xx에 정지한다.
#           -> 차정보출력한다 => 제조사, 차종류, 차번호
#--------------------------------------------------------

class car:

    # 클래스 변수
    brand='현대'

    # 인스턴스 객체 생성 및 조기화 함수
    def __init__(self,num,type,color):
        self.num=num
        self.type=type
        self.color=color

    #
    def move(self,p1,p2):
        print(f'{self.num} 자동차가 {p1}에서 {p2}로 간다.')

    def stop(self, p1):
        print(f'{self.num} 자동차가 {p1}에 정지한다.')

    def carInfo(self):
        print(f'제조사 : {car.brand}\n차종류 : {self.type}\n차번호 : {self.num}\n차색깔 : {self.color}')


# 자동차 데이터 저장 => 자동차 인스턴스 생성 => 클래스명() -- __init__()
car1=car('0101','승합차','흰색')
car1.move('집','학교')
car1.stop('주차장')
car1.carInfo()

# 정수 10개 => car 데이터 10개 저장
nums=[]
for n in range(10): nums.append(n*10)

cars=[]
for n in range(10):
    num, type, color = input('차번호, 차종류, 차색상 : '.split(','))
    cars.append(car(n*1111, 'suv','black'))

for car in cars:
    print(f'{car.num}')
    car.carInfo()

