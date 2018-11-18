from PIL import ImageGrab
from PIL import Image
import matplotlib.pyplot as plt

def Image_Classify():
    img1 = ImageGrab.grab(bbox=(0,0,1920,1080))
    img1_black = img1.convert("L")
    #img1_black.show()
    img1_black.save('fi2.png')
    
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
        if sum[i] < 1000:
            print(sum[i])
            result.append(i)
    print(result)
    if len(result) == 3:
        
        
        
        
        #1번째 그림클릭과
        print(result[0])
        print(result[1])# 클릭으로 변경
        print(result[2])
    else:
        print(result[0])
        #그리고 1번째그림 클릭
        
        
        
        
Image_Classify()





'''
plt.plot(result1)
plt.plot(result2)
plt.plot(result3)
plt.plot(result4)
plt.plot(result5)
plt.plot(result6)
plt.show()
''' 
    
