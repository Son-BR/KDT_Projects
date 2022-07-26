import os
import pandas as pd

p='./test/'

def ETT(excel):
    data=pd.read_excel(p+excel+'.xlsx')
    row=data.iloc[:,:3]                          # 모든 열,0~2행만 추출
    col=row[((row['구성 단위']=='단어') & (row['고유어 여부']=='고유어')) | ((row['구성 단위']=='단어') & (row['고유어 여부']=='한자어'))]
    col=col.rename(columns={'어휘':'가'})
    txt=col.iloc[:,:1]
    txt.to_csv(p+excel+'.txt', index=0)

# col.to_excel(p+'txt/'+ excel + '.xlsx', index=0) => 엑셀로 저장

ETT('1')