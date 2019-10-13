#매크로 만든거 읽어오
import pyautogui
import time
import csv

f = open('macro_record.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

pos = []
tim = []

for line in rdr:
    pos.append(line[0])
    tim.append(line[1])


print(pos)
time_float = list(map(float, tim))

print(time_float)

f.close()

start_t = time.time()

for i in range(len(pos)):
    position_0 = (363,768)
    position_1 = (1455, 906)

    position = position_0 if pos[i] == "0" else position_1
    
    print(position)
    pyautogui.click(position, interval = time_float[i+1])
    print (time.time()-start_t)
