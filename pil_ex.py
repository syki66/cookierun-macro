from PIL import ImageGrab
from PIL import Image
import matplotlib.pyplot as plt


#img1 = ImageGrab.grab(bbox=(0, 0, 300, 300)) #(x1,y1)부터 (x2,y2) 까지 캡처
#img1.save('abc.png')
#img2 = Image.open('abc.png')
#coordinate = (0,0)
#print(img2.getpixel(coordinate))

img1 = Image.open('pr3.png')
img1_black = img1.convert("L")
#img1.save('pr3.png')


result1 = []
result2 = []
result3 = []
for i in range(30,215):
    c = (i, 200)
    if img1_black.getpixel(c) != 239 and img1_black.getpixel(c) != 231:
        print("", img1_black.getpixel(c), end='')
        result1.append(img1_black.getpixel(c))
        
    if i % 10 == 0:
        print("")

for i in range(326, 455):
    c = (i, 200)
    if img1_black.getpixel(c) != 239 and img1_black.getpixel(c) != 231:
        print("", img1_black.getpixel(c), end='')
        result2.append(img1_black.getpixel(c))
        
    if i % 10 == 0:
        print("")
    
for i in range(606, 797):
    c = (i, 200)
    if img1_black.getpixel(c) != 239 and img1_black.getpixel(c) != 231:
        print("", img1_black.getpixel(c), end='')
        result3.append(img1_black.getpixel(c))
        
    if i % 10 == 0:
        print("")

plt.plot(result1)
plt.plot(result2)
plt.plot(result3)

for i in range(100):
    print(abs(result2[i]-result1[i]))

plt.show()
