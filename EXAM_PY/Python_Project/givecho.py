import random
import os


DIR_WORD='./word/'


# 초성 제시
def givechosung():
    randomfile = random.choice(os.listdir(DIR_WORD))
    return randomfile[:2]

while True:
    chosung=givechosung()                 #제시된 초성
    print(chosung)
    answer=input('단어 : ')+'\n'             # 플레이어 정답입력
    with open(DIR_WORD+f'{chosung}.txt',mode='r',encoding='utf-8') as txt:
        if answer == '끝내기\n':
            break
        elif answer in txt.readlines():
            print('정답')
        else:
            print('오답')
