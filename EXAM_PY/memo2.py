class Calculator:
    # 인스턴스 생성자
    def __init__(self, maker, color, *data):
        self.maker=maker
        self.color=color
        self.data=data

    # getter/setter메서드 (선택)
    def getData(self): return self.data
    def setData(self, data): self.data = data

    # 내가 원하는 계산기 기능 --------------------
    def puls(self):
        print(self.data)
        return sum(self.data)
    def showUI(self):
        print("***** 계산기 *****")
        print("1. 덧         셈")

def getNumbers():
    nums = []
    while True:
        num = input('계산 할 숫자 입력(종료 Q/q) : ')
        if num in ['q', 'Q']: break
        nums.append(int(num))
    return nums

def playApp():
    calcApp = Calculator('Shap', 'Pink')
    print('--------------START--------------')
    while True:
        calcApp.showUI()
        select = input("메뉴 선택 : ")
        if select == '5':
            break
        elif select == '1':
            calcApp.setData(getNumbers())
            print(f'덧  셈 결과 : {calcApp.puls()}')

playApp()
