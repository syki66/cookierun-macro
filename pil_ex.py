
from PIL import ImageGrab
from PIL import Image
import matplotlib.pyplot as plt

img1 = Image.open('st5.png')
img1_black = img1.convert("L")
#img1_black.show()


result1 = []
result2 = []
result3 = []
for i in range(50,150):
    c = (i,180)
    if img1_black.getpixel(c) != 239 and img1_black.getpixel(c) != 231:
        print("", img1_black.getpixel(c), end='')
        result1.append(img1_black.getpixel(c))

    if i%10 == 0 :
        print("")

print("\n========================================")

for i in range(300,400):
    c = (i,180)
    if img1_black.getpixel(c) != 239 and img1_black.getpixel(c) != 231:
        print("", img1_black.getpixel(c), end='')
        result2.append(img1_black.getpixel(c))

    if i%10 == 0 :
        print("")

print("\n========================================")

for i in range(550,650):
    c = (i,180)
    if img1_black.getpixel(c) != 239 and img1_black.getpixel(c) != 231:
        print("", img1_black.getpixel(c), end='')
        result3.append(img1_black.getpixel(c))

    if i%10 == 0 :
        print("")
print("\n========================================")

result2.insert(0,188)

for i in range(3,48):
    print(abs(result3[i]-result1[i]))




plt.plot(result1)
plt.plot(result2)
plt.plot(result3)
plt.show()




    #if img1_black.getpixel(c) != 239 and img1_black.getpixel(c) != 231: