import pyautogui
import time
import os
from PIL import Image

### 변수 설정
leftLetterBox = 174 # FHD+ 해상도용 왼쪽 레터박스 적용, 세로는 1080 고정하기

pause = 0.3 # 매크로 최소 시간 간격
failsafe = True # 안전모드. 왼쪽 위쪽으로 마우스 올리면 매크로 중단.

init_delay = 10 # 프로그램 시작후 대기시간

playtime = 300 # 플레이 시간
setCount = 10000 # 플레이 반복 횟수. 24시간 기준 약 180판 가능

ingame_pos = [
    (1085 + leftLetterBox, 400), # 점프, 부스트, 이어달리기
    (1085 + leftLetterBox, 380), # 보너스타임용 드래그
]

window_pos = [
    ((885 + leftLetterBox, 958), 3), #게임점수확인창
    ((885 + leftLetterBox, 958), 3), #보물상자 열기
    ((885 + leftLetterBox, 958), 6), #보물상자 확인
    ((1111 + leftLetterBox, 865), 3), # 00시 출첵 1 or 주간 시즌 초기화 알림표 끄기
    ((885 + leftLetterBox, 958), 3), # 00시 출첵 2
    ((1111 + leftLetterBox, 865), 3), # 00시 출첵 3
    ((1111 + leftLetterBox, 635), 3), # 시즌 초기화후 첫 점수 기록했을때 알림창 제거
    ((1156 + leftLetterBox, 705), 15), # 쿠키런앱 재실행
    ((1730 + leftLetterBox, 142), 3) # 공지 닫기
]

startgame_pos = [
    ((1733 + leftLetterBox, 963), 2), #게임시작1
    ((1600 + leftLetterBox, 914), 2) #게임시작2
]

card_delay = 10 # 매크로방지 카드 딜레이
card_pos = [ # 매크로방지 카드 좌표
            (593 + leftLetterBox, 362), (948 + leftLetterBox, 360), (1123 + leftLetterBox, 404),
            (586 + leftLetterBox, 959), (885 + leftLetterBox, 958), (1156 + leftLetterBox, 705)
        ]
card_x = [(534 + leftLetterBox, 754 + leftLetterBox), (828 + leftLetterBox, 1048 + leftLetterBox), (1121 + leftLetterBox, 1341 + leftLetterBox)] # 매크로방지게임 카드 픽셀 범위 (x축 1행, 2행)
card_y = [ # y축 1열, 2열 좌표값
            (500), 
            (885)
        ]

heart_pos = (1310 + leftLetterBox,50) # 첫번째 하트 위치 (잔량 확인)
heart_delay = 500 # 하트 소진시 딜레이 시간값

### 함수 및 실행 코드
def init(pause, failsafe):
    '''입력 간격 및 안전모드 설정'''
    pyautogui.PAUSE = pause
    pyautogui.FAILSAFE = failsafe        

def unlockCardgame(pos, x_range, y_range, delay):
    '''쿠키런 매크로 방지용 미니게임을 뚫어주는 함수'''
    os.system("scrot cardgame.png")
    img = Image.open("cardgame.png")
    capture = img.convert("L") # 흑백화

    pixels = []
    for y in y_range:
        for x in x_range:
            temp = []
            for i in range(x[0], x[1]):
                temp.append(capture.getpixel((i, y)))
            pixels.append(temp)
    
    diff = []
    for i in range(1, 6):
        sum = 0
        for j in range(len(pixels[0])):
            sum += abs(pixels[i][j]-pixels[0][j])
        diff.append((sum, i))
    diff.sort(reverse=True)

    pyautogui.click(pos[diff[0][1]])
    time.sleep(1)
    pyautogui.click(pos[diff[1][1]])
    time.sleep(delay)

def inGame(position):
    '''인게임 매크로'''
    pyautogui.click(position[0], clicks=2, interval=0.3)
    pyautogui.dragTo(position[1][0], position[1][1], 0.3, button='left')
    
def clickButtons(pos_delay):
    for pos, delay in pos_delay:
        pyautogui.click(pos)
        time.sleep(delay)

def isHeartEmpty(position):
    '''게임 플레이용 하트 잔량 체크하기'''
    os.system("scrot heart.png")
    heart_img = Image.open("heart.png")

    if heart_img.getpixel(position)[0] < 200:
        return True
    else:
        return False

def notice(delay):
    for i in range(delay):
        print(f"쿠키런 매크로가 시작됩니다. {delay - i}초 안에 현재창을 최소화시켜주세요.")
        time.sleep(1)
    print("쿠키런 매크로 진행중...")

width, height = pyautogui.size()
if not (height == 1080):
    print("해상도 높이를 1080 으로 설정해주세요.")
    print(f"현재 해상도 : {width} x {height}")
else:
    notice(init_delay)
    init(pause, failsafe)
    clickButtons(startgame_pos)
    count = 0
    start_time = time.time()
    while count < setCount:
        inGame(ingame_pos)
        elapsed_time = time.time()
        if elapsed_time - start_time > playtime:
            for _ in range(4):
                unlockCardgame(card_pos, card_x, card_y, card_delay)
            clickButtons(window_pos)
            count += 1
            print(f"{count}판 완료")
            if isHeartEmpty(heart_pos):
                time.sleep(heart_delay)
            clickButtons(startgame_pos)
            start_time = time.time()
