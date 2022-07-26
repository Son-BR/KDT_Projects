import os

count=0
for i in os.listdir('../word/'):
    with open(f'../word/{i}',mode='r',encoding='utf-8') as txt:
        txt=txt.readlines()
        count+=len(txt)
        print(i)
        print(count)