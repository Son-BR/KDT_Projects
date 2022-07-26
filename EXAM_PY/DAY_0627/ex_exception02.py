# ---------------------------------------------------------
# 프로그램 기능 구현상 강제로 예외 발생시키기
# rasie 예외 객체
# ---------------------------------------------------------

num=int(input('3의 배수 입력 : '))

try:
    if num%3!=0:
        print(f'{num}은 3의 배수가 아닙니다.')
        raise Exception('3의 배수 오류')
except Exception:
    print('ERROR 발생')


class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

e=Eagle()
e.fly()