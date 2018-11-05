import pyautogui
import sys
import time

#마우스 위치이동
pyautogui.moveTo(100, 150)

#모니터 해상도 가져오
width, height = pyautogui.size()  
print('width={0}, height={1}'.format(width, height))

#안전모드, 에러시 탈출구
pyautogui.PAUSE = 1  
pyautogui.FAILSAFE = True

#특정문자열 입력
pyautogui.typewrite('Hello!')
pyautogui.typewrite('gksrmf', interval = 0.25)

#드래그
pyautogui.dragTo(x=100, y=100, duration=2)
