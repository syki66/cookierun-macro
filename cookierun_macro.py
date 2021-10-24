import pyautogui
import sys
import time
import image
#import pytesseract
# from PIL import ImageGrab
import os
from PIL import Image

width, height = pyautogui.size()
print("================================================================")
print("쿠키런매크로")
print("현재해상도:", width, height)
print("해상도 1920x1080에서 전체화면에서만 정상동작")
print("================================================================")

#안전모드, 에러시 탈출구 (마우스 왼쪽 위 모서리에 가져가면 에러 송출)
pyautogui.PAUSE = 0.3 #메쏘드간 대기시간
pyautogui.FAILSAFE = True


#쿠키런 매크로 방지 뚫는 함수

img_position = [(593, 362),(948, 360),(1123, 404),(586, 959),(883, 986),(1156, 705)]

def Image_Classify():
    os.system("scrot screenshot.png")
    img1 = Image.open("screenshot.png")
    img1_black = img1.convert("L")
    #img1_black.show()
    #img1_black.save('fi2.png')
    
    #(534,500)얘가 기준값
    result1 = []
    result2 = []
    result3 = []
    result4 = []
    result5 = []
    result6 = []
    

    img_y1 = 500
    img_y2 = 885
    for i in range(534,754):
        c = (i, img_y1)
        result1.append(img1_black.getpixel(c))

    for i in range(534,754):
        c = (i, img_y2)
        result4.append(img1_black.getpixel(c))
            
    for i in range(828,1048):
        c = (i, img_y1)
        result2.append(img1_black.getpixel(c))
        
    for i in range(828,1048):
        c = (i, img_y2)
        result5.append(img1_black.getpixel(c))
            
    for i in range(1121,1341):
        c = (i, img_y1)
        result3.append(img1_black.getpixel(c))
            
    for i in range(1121,1341):
        c = (i, img_y2)
        result6.append(img1_black.getpixel(c))
    
    sum = [0,0,0,0,0]    
    
    for i in range(len(result1)):
        sum[0] += abs(result2[i]-result1[i])
        
    for i in range(len(result1)):
        sum[1] += abs(result3[i]-result1[i])
        
    for i in range(len(result1)):
        sum[2] += abs(result4[i]-result1[i])
    
    for i in range(len(result1)):
        sum[3] += abs(result5[i]-result1[i])
        
    for i in range(len(result1)):
        sum[4] += abs(result6[i]-result1[i])

    for i in range(len(sum)):
        print("값",i," : ", sum[i])
    
    result = []
    for i in range(len(sum)):
        if sum[i] > 1300:
            print(sum[i])
            result.append(i+1) #두번째그림이 sum[0]이라서 1추가함
    print("차출된값: ", result)
    
    #첫번째값이 기준값일경우
    if len(result) == 2:
        #다른 두개그림 클릭
        time.sleep(2)
        pyautogui.click(img_position[result[0]])
        time.sleep(2)
        pyautogui.click(img_position[result[1]])
        time.sleep(2)
        
    #첫번째 값이 다른값일 경우
    elif len(result) == 4:
        time.sleep(2)
        pyautogui.click(img_position[0])
        time.sleep(2)
        if 1 not in result:
            pyautogui.click(img_position[1])
        elif 2 not in result:
            pyautogui.click(img_position[2])
        elif 3 not in result:
            pyautogui.click(img_position[3])
        elif 4 not in result:
            pyautogui.click(img_position[4])
        elif 5 not in result:
            pyautogui.click(img_position[5])
        else:
            pass
        time.sleep(2)


        
        #첫번째값과 나머지하나클릭

    #매크로가 뜨지 않을경우
    else:
        pass



#인게임 매크로
game_count = 0
start_t = time.time()
time.sleep(2)
pyautogui.click(1620, 914) #게임시작2

while(True):
    
    pyautogui.click(1620, 914) #점프
    pyautogui.click(958,400) # 슬라이드 및 부스트 및 이어달리기
    pyautogui.dragTo(958,380, 0.5, button='left') # 슬라이드 용 드래그
    pyautogui.click(1620, 914) #점프
    
    end_t = time.time()
    
    if (end_t - start_t) > 240:
        game_count += 1 #게임 판수 세기
        print("******************************", game_count,"판")
        #start_t = end_t
        time.sleep(5)
        for i in range(4):
            time.sleep(1)
            Image_Classify() #매크로방지 뚫기함수
            time.sleep(1)


        time.sleep(1)
        pyautogui.click(883, 986) #게임점수확인창(자랑하기 x축 984~1458, y축 887~ 보물상자 동일)
        time.sleep(2)

        pyautogui.click(885,958) #보물상자 열기
        time.sleep(2)
        pyautogui.click(885,958) #보물상자 확인
        time.sleep(9)
        pyautogui.click(1111,865) # 00시 출첵 1 or 주간 시즌 초기화 알림표 끄기
        time.sleep(2)
        pyautogui.click(885,958) # 00시 출첵 2
        time.sleep(2)
        pyautogui.click(1111,865) # 00시 출첵 3
        time.sleep(2)

        pyautogui.click(1111,635) # 시즌 초기화후 첫 점수 기록했을때 알림창 제거
        time.sleep(1)


        os.system("scrot screenshot.png")
        heart_check = Image.open("screenshot.png") #하트 다떨어졌을시 500초 대기 (하트 충전시간은 8분)
        if (heart_check.getpixel((1310,50))!=(255,0,0)):
            print("생명 충전중....")
            time.sleep(500)
            start_t = time.time()
        else:
            start_t = time.time()
        pyautogui.click(1733, 963) #게임시작1
        time.sleep(1)
        pyautogui.click(1600, 914) #게임시작 2
        time.sleep(1)

