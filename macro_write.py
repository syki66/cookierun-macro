from pynput.mouse import Listener
import pyautogui
import time
import csv

csvfile = open("macro_record.csv", "w", newline="")
csvwriter = csv.writer(csvfile)

full_data = []

start_time = time.time()


def is_clicked(x, y, button, pressed):
    if pressed:
        x_pos = 0 if pyautogui.position()[0]<960 else 1
        running_time = (time.time()-start_time)
        each_data = [x_pos, running_time]
        full_data.append(each_data)
        print(each_data)

        if (time.time() - start_time > 20):
            
            for row in full_data:
                csvwriter.writerow(row)

            csvfile.close()


with Listener(on_click=is_clicked) as listener:
    listener.join()



