# 모듈
import pandas
import os
import re

# 폴더
ori='./dic/'                    # 처리할 엑셀파일 위치
DIR_WORD='./word/'              # 최종 txt 파일 저장 폴더


# 함수 정의

# 엑셀 처리후 txt로 변환
def ETT(excel):
    if not os.path.exists(DIR_WORD+'ETT/'): os.mkdir(DIR_WORD+'ETT/')
    data = pandas.read_excel(ori + excel)
    row=data.iloc[:,:3]
    col=row[((row['구성 단위']=='단어') & (row['고유어 여부']=='고유어')) | ((row['구성 단위']=='단어') & (row['고유어 여부']=='한자어'))]
    col=col.rename(columns={'어휘':'가'})
    txt=col.iloc[:,:1]
    txt.to_csv(DIR_WORD+'ETT/'+excel[:-5]+'.txt', index=0)

# 한글 제외한 모든 문자 제거
def clean_txt(txt_file):
    if not os.path.exists(DIR_WORD+'clean_txt'): os.mkdir(DIR_WORD+'clean_txt')
    with open(DIR_WORD+'ETT/'+txt_file,mode='r',encoding='utf-8') as txt:
        with open(DIR_WORD+'clean_txt/'+txt_file,mode='w',encoding='utf-8') as txt2:
            while True:
                word=txt.readline()
                word=re.sub('[^가-힣]','', word)
                txt2.write(word+'\n')
                if not word: break

# 2글자 아닌 단어 제거
def wordTwo(txt_file):
    if not os.path.exists(DIR_WORD+'wordTwo'): os.mkdir(DIR_WORD+'wordTwo')
    with open(DIR_WORD+'clean_txt/'+txt_file,mode='r',encoding='utf-8') as txt:
        with open(DIR_WORD+'wordTwo/'+txt_file, mode='w',encoding='utf-8') as txt2:
            while True:
                word=txt.readline()
                if len(word)==3:
                    txt2.write(word)
                elif not word:
                    break
                else: pass

# 중복제거
def set_txt(txt_file):
    if not os.path.exists(DIR_WORD+'set_txt'): os.mkdir(DIR_WORD+'set_txt')
    with open(DIR_WORD+'wordTwo/'+txt_file,mode='r',encoding='utf-8') as txt:
        with open(DIR_WORD+'set_txt/'+txt_file,mode='w',encoding='utf-8') as txt2:
            txtList = list(set(txt.readlines()))
            txtList.sort()
            for i in txtList: txt2.write(i)

# 초성 판별 후 ㄱㄱ~ㅎㅎ.txt에 각각 저장
def chosung(txt_file):
    chosungList = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
    with open(DIR_WORD+'set_txt/'+txt_file,mode='r',encoding='utf-8') as txt:
        while True:
            word=txt.readline().strip()
            chosung1=''
            if not word: break
            else:
                for i in list(word):
                    code=((ord(i)-ord('가'))//588)
                    chosung1+=chosungList[code]
                with open(DIR_WORD+chosung1+'.txt',mode='a',encoding='utf-8') as txt2:
                    txt2.write(word+'\n')

# 폴더 내 파일 개수 반환
def count_file(dir_path):
    dir_count= os.listdir(dir_path)
    return len(dir_count)

# 기능 구현
if count_file(DIR_WORD)!=351:
    excelList=os.listdir(ori)
    for i in excelList:
        ETT(i)
        i=i[:-5]+'.txt'
        clean_txt(i)
        wordTwo(i)
        set_txt(i)
        chosung(i)

    # 필요없는 파일,폴더 삭제
    reList=os.listdir(DIR_WORD)
    dirlist=[]
    for i in reList:
        if not '.txt' in i:
            dirlist+=[i]
    for i in dirlist:
        for j in os.listdir(DIR_WORD+i):
            os.remove(DIR_WORD+i+'/'+j)
        os.rmdir(DIR_WORD+i)


from tkinter import *
import tkinter.font
import tkinter.ttk


# 메인 UI
w = Tk()
w.title("초성 Quiz!")
w.geometry("400x297")


# 메인 이미지 넣기
photo = PhotoImage(file="./image/example2.png")
pLabel = Label(w, image=photo)
pLabel.pack(expand=1, anchor=N)             #화면비(?), 가운데정렬


# 랭킹페이지 새창 생성
def create_rank_page():
    newWindow = Toplevel(w)
    newWindow.title('랭킹현황')
    newWindow.geometry("250x297")
    rank = Label(newWindow, text='순위', fg='blue')
    rank.place(x=20, y=10)
    name = Label(newWindow, text='닉네임', fg='red')
    name.place(x=75, y=10)
    score = Label(newWindow, text='점수', fg='purple')
    score.place(x=145, y=10)
    time = Label(newWindow, text='시간', fg='green')
    time.place(x=200, y=10)
    listbox = Listbox(newWindow, width=32, height=15)
    listbox.place(x=10, y=40)


# 게임 설명 페이지
def create_how_page():
    newWindow = Toplevel(w)
    newWindow.title('게임 설명')
    newWindow.geometry("500x500")
    page = PhotoImage(file='../image/guide.png')
    page_label = tkinter.Label(newWindow, image=page)
    page_label.place(x=0, y=0)


# 게임 페이지 새창 생성
def create_game_page():
    newWindow = Toplevel(w)
    newWindow.title('초성 Quiz!')
    newWindow.geometry("400x297")
    # 버튼들
    how_btn = Button(newWindow, text='게임설명', height=3, width=17, command=create_how_page)
    how_btn.place(x=1, y=240)
    start_btn = Button(newWindow, text='게임시작!', height=3, width=17)
    start_btn.place(x=135, y=240)
    exit_btn2 = Button(newWindow, text='종   료', height=3, width=17, command=newWindow.destroy)
    exit_btn2.place(x=270, y=240)
    # 초성 표시 부분
    chosung1 = Label(newWindow, height=4, width=10, anchor='center', relief='ridge', borderwidth=5)
    chosung1.place(x=110, y=70)
    chosung2 = Label(newWindow, height=4, width=10, anchor='center', relief='ridge', borderwidth=5)
    chosung2.place(x=200, y=70)
    # 남은시간 타이머
    curr_progress = tkinter.DoubleVar()
    progress_bar = tkinter.ttk.Progressbar(newWindow, length=190, maximum=100, value=30)
    progress_bar.place(x=100, y=155)
    # 초성 입력 부분
    font = tkinter.font.Font(size=20)
    chosung_input = Entry(newWindow, width=12, font=font, justify='center')
    chosung_input.place(x=98, y=190)
    # 라운드 수 표시
    font2 = tkinter.font.Font(size=15, weight='bold')
    round = Label(newWindow, text='라운드 : ',width=12, font=font2, justify='center')
    count = Label(newWindow, text='정답수 : ', width=12, font=font2, justify='center')
    round.place(x=85, y=10)
    count.place(x=85, y=40)


# 랭킹보기 버튼
rank_btn = Button(text='랭킹보기', height=3, width=17, command=create_rank_page)
rank_btn.place(x=1, y=240)


# 퀴즈풀러 가기 버튼
quiz_btn = Button(text='퀴즈풀러 가기', height=3, width=17, command=create_game_page)
quiz_btn.place(x=135, y=240)


# 종료 기능 선언
def close_window():
    w.destroy()


# 종료 버튼 구현
exit_btn = Button(text='종   료', height=3, width=17, command=close_window)
exit_btn.place(x=270, y=240)


# 메인UI 구동
w.mainloop()