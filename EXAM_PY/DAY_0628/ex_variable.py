# ---------------------------------------------------
# 변수의 스코프(Scope)
# - 지역변수(Local Variable) : 함수에서만 사용, 파라미터, 함수안에 변수들
# - 전역변수(Global Variable) : 파이썬 파일안에 있는 변수,
#                             값은 파이썬 파일안에 있는 함수에서 사용가능
# ---------------------------------------------------

isGame=False

# 게임 시작을 알리는 함수
def startGame():
    global isGame
    print('*** 게 임 시 작 ***')
    isGame=True

# 게임 화면을 그려주는 함수
# 게임중일때 => 게임판 그리고
# 개암중 아닐때 => 준비중 그려주기
def drowGame():
    if isGame:
        print('********************************')
        print('*                              *')
        print('*                              *')
        print('*                              *')
        print('*                              *')
        print('********************************')
    else:
        print('*      준       비       중      *')


# 테스트
drowGame()
startGame()
drowGame()