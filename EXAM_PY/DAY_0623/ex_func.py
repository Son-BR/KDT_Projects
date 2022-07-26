# --------------------------------------------------------------
# 함수 (Function) : 자주 사용되는 기능을 묶어서 이름을 붙여 놓은 것
# - 코드 재사용 위한 것
# 형태
# def 함수명(재료,........, 재료n):
#   코드
#   코드
#   return 결과
# --------------------------------------------------------------
# --------------------------------------------------------------
# 기 능 : 숫자 2개 더한 후 결과 돌려주는 기능
# 함수명 : addTwo
# 재료(매개변수) : num1, num2
# 결과(반환값) : 더한 값
# --------------------------------------------------------------

# num2=0 -> 디폴트밸류
def addTwo(num1, num2=0):
    '''
    숫자 2개 더한 후 결과 반환
    :param num1: int
    :param num2: int
    :return: int
    '''
    value=num1+num2
    return value

# 함수 사용하기 => 함수 호출
result=addTwo(10, 20)

# 화면에 출력하기 => print(데이터)
print(result)

# --------------------------------------------------------------
# 기  능 : 문자 2개 더하는 기능의 함수
# 함수명 : strTwo
# 재  료 : str1, str2
# 반  환 : str1+str2

def strTwo(str1,str2):
    return str1+str2

# --------------------------------------------------------------
# 기  능 : 원하는 단의 구구단을 출력하는 기능의 함수
# 함수명 : multi
# 재  료 : int1
# 반  환 :

def multi(int1):
    for i in range(1,10):
        print(int1*i)
# --------------------------------------------------------------
# 가변인자 함수 => 매개변수 0개 - N개
def addNum(*nums):      # *nums -> 튜플타입으로 저장
    print(f'nums type : {type(nums)}')
    total=0
    for num in nums: total+=num
    return total

print(addNum(1,2,3,4,5,6))

# --------------------------------------------------------------
# 기    능 : 평균 구하는 함수
# 함 수 명 : getAvg
# 파라미터 : 과목명 - 점수 유동적 => **subjects
# 반 환 값 : 평균 --- float
# --------------------------------------------------------------

# 키워드 파라미터 -> 숫자 불가, 따옴표 없어아햠
def getAvg(**subjets):
    print(f'subjetcs type : {type(subjets)}')
    values=subjets.values()
    total=0
    for value in values: total+=value
    print(f'total : {total}')
    return total/len(values) if len(values)>0 else None

print(getAvg(국어=12, 영어=98, 수학=88))
print(getAvg())

# --------------------------------------------------------------
# 함수(function)의 데이터 타입 => class function
# --------------------------------------------------------------
print(type(addTwo),id(addTwo))

list=[addTwo, getAvg]

print(list[0](1,2))
print(list[1](국어=12,영어=98,수학=88))