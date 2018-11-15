import pyautogui
import sys
import time
import image
import pytesseract
from PIL import ImageGrab



#모니터 해상도 가져오기
width, height = pyautogui.size()  
print('width={0}, height={1}'.format(width, height))

#안전모드, 에러시 탈출구 (마우스 왼쪽 위 모서리에 가져가면 에러 송출)
pyautogui.PAUSE = 0.6 #메쏘드간 대기시간
pyautogui.FAILSAFE = True

#매크로

start_t = time.time()
time.sleep(2)
pyautogui.click(1590, 893)
while(True):
    pyautogui.doubleClick(1815, 469)
    pyautogui.click(1815, 469)
    pyautogui.click(1080, 531)
    end_t = time.time()
    
    if (end_t - start_t) > 340:
        start_t = end_t
        time.sleep(5)
        pyautogui.click(689, 936) #게임점수확인창(자랑하기 y축 870~1008, 보물상자 동일)
        time.sleep(3)
        pyautogui.click(884, 970) #보물상자 열기
        time.sleep(3)
        pyautogui.click(884, 970) #보물상자 확인
        time.sleep(2)
        pyautogui.click(1573, 277) #보물상자 없을시 포춘쿠키창 끄기
        time.sleep(2)
        pyautogui.click(1590, 893) #게임시작1
        time.sleep(2)
        pyautogui.click(1590, 893) #게임시작 2
        


#이미지 추출
#img1 = ImageGrab.grab(bbox=(0, 0, 300, 300))
#img1.show()

#print(pytesseract.image_to_string(img1))


#print(pyautogui.position())
