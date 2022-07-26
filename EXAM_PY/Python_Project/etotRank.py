# 모듈
import pandas

def rankexcel(excel):
    data = pandas.read_excel(excel)
    row=data.iloc[:,:5]
    row.to_csv('rank.txt', index=0)

rankexcel('./rank.xlsx')