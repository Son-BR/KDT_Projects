# ----------------------------------------------------------------------
# 모듈(Module) : 하나의 파이썬(.py) 파일
#               특정 목적에 관련된 변수, 함수, 클래스 존재
#               필요한 파일에서 사용 가능 함
# 사용법 => import 모듈명
# ----------------------------------------------------------------------
# 모듈 포함하기
# import math as m                    # m으로 math모듈 가져오기
from math import factorial, pi, fabs  # 모듈에서 특정 기능만 가져오기

# 모듈 안의 기능 시용하기
# print(mate.factorial(5))
print(factorial(5), pi, fabs(2))

# ----------------------------------------------------------------------
import ex_func

print(ex_func.YEAR, ex_func.printYear())


