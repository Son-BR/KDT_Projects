import time
import pandas as pd
import os
import openpyxl
import random
DIR_WORD_PATH='./word'
DIRC_EXCEL='./rank.xlsx'

randomfile=random.choice(os.listdir(DIR_WORD_PATH))

print(randomfile)