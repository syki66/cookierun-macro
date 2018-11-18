from PIL import ImageGrab
from PIL import Image
import matplotlib.pyplot as plt


img1 = ImageGrab.grab(bbox=(0,0,1920,1080))
img1_black = img1.convert("L")
img1_black.show()
img1_black.save('fi2.png')

#(548,526) , (548,887)    x좌표 768까지

result1 = []
result2 = []
#+ 220픽셀 비교
#첫번째 이미지 (548,526)  ,,기준으로 나머지 5개 비교하기
#두번째 이미지 (823,526)
#세번째 이미지 (1098,526)
#네번째 이미지 (548,887)
#오번째 이미지 (823,887)
#육번째 이미지 (1098,887)
#
for i in range(548,768):
    c = (i, 526)
    print("", img1_black.getpixel(c), end='')
    result1.append(img1_black.getpixel(c))
    if i % 10 == 0:
        print("")

for i in range(548,768):
    c = (i, 887)
    print("", img1_black.getpixel(c), end='')
    result2.append(img1_black.getpixel(c))
    if i % 10 == 0:
        print("")
    
    
plt.plot(result1)
plt.plot(result2)

#합계 기준 1000으로 1000보다 같으면 동일이미

'''
sum = 0
for i in range(len(result1)):
    sum += abs(result2[i]-result1[i])
    
print("합계는", sum)
'''