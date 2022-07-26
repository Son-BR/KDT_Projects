# ---------------------------------------------------------
# 사용자 정의 클래스 => 학생을 표현하는 데이터 타입
# ---------------------------------------------------------
# 특징/성질/외형 => 변수 -- 필드/속성(field/Attribute)
#                  교복, 학교, 성적, 학년, 반, 학번 ...
# 역할/기능      => 함수 -- 메서드
#                   공부한다, 학교에간다, 시험친다, ...
# ---------------------------------------------------------
# 클래스명 => student
# 속   성 => 학번, 학교, 학년, 석차
# 역   학 => 공부하다, 시험친다
# ---------------------------------------------------------

class student:
    # 클래스 변수 --> 모든 인스턴스가 함께 사용함
    school='대구중학교'

    # 인스턴스(객체) 생성시 초기화 메서드
    def __init__(self, stdnum, yearnum,grade):
        self.stdnum=stdnum
        self.yearnum=yearnum
        self.grade=grade

    # student의 클래스 역할/기능 메서드

    # 000이 00을 공부한다
    def study(self,subject):
        print(f'{self.stdnum}은 {subject}과목을 공부한다.')

    # 000이 00시험을 친다
    def test(self, title):
        print(f'{self.stdnum}은 {title}시험을 친다.')

    # 학생정보 출력 기능
    # 학번, 학년, 학교 정보 출력
    def displayInfo(self):
        print(f'학교 : {student.school}') # student.school // self.school
        print(f'학번 : {self.stdnum}')
        print(f'학년 : {self.yearnum}')

# 객체 즉 student 인스턴스(Instance) 생성

std1=student('std001',1,10)
std2=student('std002',1,8)
std3=student('kn0101',3,15)

# 메서드 실행
std1.displayInfo()
