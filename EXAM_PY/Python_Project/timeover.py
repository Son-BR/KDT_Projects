import time
import inputimeout





# start_time=time.time()
#
while True:
    timeflow = time.time() - start_time
    if timeflow>=5:
        print('Game Over')
        break
    else:
        input('게임진행')

try:
    key=inputimeout.inputimeout('초성입력:',timeout=5)
except inputimeout.TimeoutOccurred:
    key='Game Over'
    print(key)
