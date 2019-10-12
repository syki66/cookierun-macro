#매크로 만든거 읽어오
import pyautogui
import time
import csv

pyautogui.PAUSE = 0
f = open('macro_record.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

pos = []
tim = []

for line in rdr:
    pos.append(line[0])
    tim.append(line[1])



time_float = list(map(float, tim))



f.close()


for i in range(len(pos)):
    start_t = time.time()
    position_0 = (363,768)
    position_1 = (1455, 906)

    position = position_0 if pos[i] == "0" else position_1
    
    time.sleep(time_float[i+1])

    pyautogui.click(position)

