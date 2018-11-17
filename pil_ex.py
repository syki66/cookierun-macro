import pyautogui
from PIL import ImageGrab
from PIL import Image

#img1 = ImageGrab.grab(bbox=(0, 0, 300, 300)) #(x1,y1)부터 (x2,y2) 까지 캡처
#img1.save('abc.png')
#img2 = Image.open('abc.png')
#coordinate = (0,0)
#print(img2.getpixel(coordinate))

img1 = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
img1.show()

c1_result = []
for i in range(349,528):
    c = (i,218)
    c1_result.append(list(img1.getpixel(c)))
    #print(",",i, "--", img1.getpixel(c), end='')
    
    #if i % 10 == 0:
    #    print("")

c2_result = []
for i in range(545,724):
    c1 = (i, 218)
    c2_result.append(list(img1.getpixel(c)))
print(c1_result)


'''
img2 = ImageGrab.grab(bbox=(524, 293, 1071, 294))
img2.show()
'''
#print(pyautogui.position())

#349~527

#545~723
