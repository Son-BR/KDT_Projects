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
filename='comment.txt'
with open(filename,mode='a',encoding='utf-8') as f:
    while True:
        txt = input("댓글 입력 : ")
        if txt in ['q', 'Q'] : break
        print(f'txt => {txt}')
        f.write(txt+'\n')

# ------------------------------------------------------------------
# [조건]
# - home.html 파일을 복사해서 home.txt 파일로 만들기
# - 함 수 명 : fileCopy
# - 매개변수 : 파일명
# - 반 환 값 : 없음
# ------------------------------------------------------------------
def fileCopy(filename):
    # 원본파일 열고 데이터 꺼내기
    print(f'filename => {filename}')
    srcFile=open(filename,mode='r',encoding='utf-8')
    data=srcFile.read()
    srcFile.close()

    # 복사본 파일에 데이터 쓰기
        # home.html => home.txt
        # [:'home.html'.index('.')]
        # filename.split('.')[0]
    print(f'filename => {filename}')
    filename=filename[:filename.rindex(".")]+'.txt'
    desFile=open(filename,mode='w',encoding='utf-8')
    desFile.write(data)
    desFile.close()

filename='./html/home.html'

print(f'"."의 인덱스 => {filename.index(".")}')
print(f'"."의 인덱스 => {filename.rindex(".")}')
print(f'확장자 제거 => {filename[:filename.rindex(".")]}')

fileCopy(filename)

def fileCopy(filename):
    # 복사 파일명 생성
    newFilename = filename[:filename.rindex(".")] + '.txt'
    # 파일 데이터 복사
    with open(filename,mode='w',encoding='utf-8') as srcFile:
        with open(newFilename, mode='w', encoding='utf-8') as desFile:
            desFile.write(srcFile.read())

