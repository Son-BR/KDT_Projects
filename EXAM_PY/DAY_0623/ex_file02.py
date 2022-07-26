# ---------------------------------------------------------------------------
# PATH => 경로
# - 절대경로 : 파일 및 폴더 존재하는 위치의 경로 예) C:\Users\User\PycharmProjects\EXAM_PY\DAY_0623\mydata.txt .....
# - 상대경로 : 현재 코드 파일 기준으로 경로를 지정
#   . : 현재위치
#  .. : 상위 한 단계 위
# ---------------------------------------------------------------------------
file=r'C:\Users\User\PycharmProjects\EXAM_PY\DAY_0623\mydata.txt'
file='../Data/home.html'
file='./html/home.html'

# home.html 파일을 라인단위로 읽어서 화면에 출력하기

# 파일 열기
file=open(file,mode='r',encoding='utf-8')

# 파읽 읽기
while True:
    data=file.readline()
    if not data : break
    data=data.strip()
    if len(data)>0 : print(data)

# 파일 닫기
file.close()


# with - as 구문
file='./html/home.html'
with open(file, mode='r', encoding='utf-8') as file:
    while True:
        data = file.readline()
        if not data: break
        data = data.strip()
        if len(data) > 0: print(data)
