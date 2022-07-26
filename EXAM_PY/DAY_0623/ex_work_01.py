# ------------------------------------------------------------------
# 사용자가 입력한 댓글을 파일로 저장하기
# [조건]
# - 키보드로 댓글 입력 받기 => input()
# - 입력받은 댓글 누적 하기
# - 댓글 입력 종료 조건으로 q 또는 Q 입력시 댓글 입력 종료
# ------------------------------------------------------------------

# input() 내장함수
# - 매개변수 : 입력받고 싶은 데이터 요청 메시지 str타입
# - 결   과 : 입력받은 데이터 => str타입

# ------------------------------------------------------------------

filename='reple.txt'

file=open(filename, mode='a', encoding='utf-8')

while True:
    reple1=input("댓글 입력")
    if reple1=='q' or reple1=='Q':
        break
    file.write(reple1+'\n')

file.close()

file=open(filename, mode='r', encoding='utf-8')
print(file.read())
file.close()

# ------------------------------------------------------------------
# [조건]
# - home.html 파일을 복사해서 home.txt 파일로 만들기
# - 함 수 명 : fileCopy
# - 매개변수 : 파일명
# - 반 환 값 : 없음
# ------------------------------------------------------------------
file='../Data/home.html'
def fileCopy(file):
    txt='home.txt'
    with open(file, mode='r', encoding='utf-8') as file:
        with open(txt, mode='w', encoding='utf-8') as txt:
            txt.write(file.read())

fileCopy(file)


