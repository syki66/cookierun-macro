import csv
import pyautogui
import time
from PIL import ImageGrab


pyautogui.click(1600, 914) # 게임시작 2

f = open('sudong.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)


pos = []
tim = []

for line in rdr:
    pos.append(line[0])
    tim.append(line[1])

time_float = list(map(float, tim))


time.sleep(4.5)

for i in range(len(pos)):
    position_1 = (1455, 906)
    pyautogui.click(position_1, interval = time_float[i])
