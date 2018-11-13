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
pyautogui.PAUSE = 1 #메쏘드간 대기시간
pyautogui.FAILSAFE = True

#매크로


start_t = time.time()

while(True):
    pyautogui.click(1400, 600)
    pyautogui.click(1400, 600)
    pyautogui.click(950,540)
    end_t = time.time()
    
    if (end_t - start_t) > 300:
        start_t = end_t
        time.sleep(10)
        pyautogui.click(689, 936) #게임점수확인창
        time.sleep(5)
        pyautogui.click(1083, 937) #보물상자 열기
        time.sleep(5)
        pyautogui.click(1083, 937) #보물상자 확인
        time.sleep(5)
        pyautogui.click(1522,937) #게임시작1
        time.sleep(5)
        pyautogui.click(1522,937) #게임시작 2
        


#이미지 추출
#img1 = ImageGrab.grab(bbox=(0, 0, 300, 300))
#img1.show()

#print(pytesseract.image_to_string(img1))
