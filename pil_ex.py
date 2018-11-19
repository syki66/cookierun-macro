img_position = [(558, 315),(867, 317),(1102, 595),(592, 773),(926, 952),(1106, 678)]
import time

def Image_Classify():
    img1 = ImageGrab.grab(bbox=(0,0,1920,1080))
    img1_black = img1.convert("L")
    #img1_black.show()
    #img1_black.save('fi2.png')
    
    #(548,526)얘가 기준값 , (548,886)    x좌표 768까지
    result1 = []
    result2 = []
    result3 = []
    result4 = []
    result5 = []
    result6 = []
    
    for i in range(548,768):
        c = (i, 526)
        result1.append(img1_black.getpixel(c))
    
    for i in range(548,768):
        c = (i, 887)
        result4.append(img1_black.getpixel(c))
        
    for i in range(823,1043):
        c = (i, 526)
        result2.append(img1_black.getpixel(c))
    
    for i in range(823,1043):
        c = (i, 887)
        result5.append(img1_black.getpixel(c))
        
    for i in range(1098,1318):
        c = (i, 526)
        result3.append(img1_black.getpixel(c))
        
    for i in range(1098,1318):
        c = (i, 887)
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
    
    result = []
    for i in range(len(sum)):
        if sum[i] > 1000:
            print(sum[i])
            result.append(i+1) #두번째그림이 sum[0]이라서 1추가함
    print(result)
    
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

for i in range(6):
    time.sleep(2)
    Image_Classify() #매크로방지 뚫기함수
    time.sleep(2)
