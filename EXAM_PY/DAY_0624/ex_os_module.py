# -------------------------------------------------------------
# File & Dir 관련 모듈
# -------------------------------------------------------------
import os.path as path
import os


# 특정 폴더 존재여부 체크 => 폴더 없으면 폴더 생성하기
DIR_PATH='./DATA/jpg/000'
# print(path.exists(DIR_PATH))
if not path.exists(DIR_PATH) :
    # os.mkdir(DIR_PATH)        # 1개 폴더 생성
    os.makedirs(DIR_PATH)       # 하위 폴더까지 생성

# 특정 파일 존재여부 체크
DATA_FILE=DIR_PATH+'/flower.jpg'
if not path.exists(DATA_FILE):
    print('파일 없음')

# 특정 경로 안에 존재하는 내용 리스트화
dataList=os.listdir('./AddressBook')
print(dataList)

# 시간 관련 모듈
import time as t
print(t.time())
print(t.localtime(t.time()))

curTime=t.localtime(t.time())
print(curTime.tm_year, curTime.tm_hour, curTime.tm_wday)


for num in range(10):
    t.sleep(0.5)        # 0.5초 멈춤
    print(num,end=' ')