# --------------------------------------------------------------
# 벽돌깨기 프로그램 만들기
# --------------------------------------------------------------

# 게임하는 사람의 정보를 저장하는 변수들
nickName=''
level=0
score=0
ranking=0
player1 = None
player2 = None
# --------------------------------------------------------------

# 클래스
class player:

    def __init__(self, nickname,level=0,score=0,ranking=0):
        self.nickname = nickname
        self.level = 0
        self.score = 0
        self.ranking = 0

    # 클래스의 인스턴스 변수들의 값을 업데이트 또는 읽기하는 메서드
    # set메서드, get메서드
    def setnickname(self, nickname):
        self.nickname = nickname

    def setlevel(self, level):
        self.level = level

    def setscore(self, score):
        self.score = score

    def setranking(self, ranking):
        self.ranking = ranking

    def setupdate(self, level, score, ranking):
        self.level = level
        self.score = score
        self.ranking = ranking

    def getnickname(self):
        return self.nickname

    def getlevel(self):
        return self.level

    def getscore(self):
        return self.score

    def getranking(self):
        return self.ranking

# 게임하는 사람의 정보 입력 받기
# 함 수 명 : setPlayer
# 파라미터 : 없음
# 반 환 값 : 없음
def setPlayer():
    nickname=input('닉네임 :')
    global player1
    if player1 == None :             #player1 전역변수 지정해야 함
        player1=player(nickname)

# --------------------------------------------------------------

# 메뉴 출력하기
# 함 수 명 : displayMenu
# 파라미터 : 없음
# 반 환 값 : 없음
def displayMenu():
    print('1.회원가입')
    print('2.게임 시작')
    print('3.랭킹보기')
    print('4.종료')

def playGame():
    level=3
    score=158
    ranking=5

# --------------------------------------------------------------
# 프로그램 코드
while True:
    displayMenu()
    select=input('메뉴 선택 : ')
    if select=='4':
        # 파일게 기록하고 종료

        break
    elif select=='1':
        setPlayer()

# --------------------------------------------------------------







