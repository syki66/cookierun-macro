import pyautogui
import time
import os
from PIL import Image

### 변수 설정
pause = 0.3 # 매크로 최소 시간 간격
failsafe = True # 안전모드. 왼쪽 위쪽으로 마우스 올리면 매크로 중단.

playtime = 240 # 플레이 시간
setCount = 100 # 플레이 반복 횟수

ingame_pos = [
    (1620, 914), # 점프
    (958, 395), # 슬라이드 및 부스트 및 이어달리기
    (958, 380, 0.5), # 슬라이드 용 드래그
]

window_pos = [
    ((883, 986), 2), #게임점수확인창
    ((1640, 280), 2), # 행운쿠키 창 닫기
    ((885, 958), 2), #보물상자 열기
    ((885, 958), 10), #보물상자 확인
    ((1111, 865), 2), # 00시 출첵 1 or 주간 시즌 초기화 알림표 끄기
    ((885, 958), 2), # 00시 출첵 2
    ((1111, 865), 2), # 00시 출첵 3
    ((1111, 635), 1), # 시즌 초기화후 첫 점수 기록했을때 알림창 제거
]

startgame_pos = [
    ((1733, 963), 1), #게임시작1
    ((1600, 914), 1) #게임시작2
]

card_delay = 3 # 매크로방지 카드 딜레이

card_pos = [ # 매크로방지 카드 좌표
    (593, 362), (948, 360), (1123, 404),
    (586, 959), (883, 986), (1156, 705)
]

card_x = [(534,754), (828,1048), (1121,1341)] # 매크로방지게임 카드 픽셀 범위 (x축 1행, 2행)
card_y = [ # y축 1열, 2열 좌표값
            (500), 
            (885)
        ]

heart_pos = (1310,50) # 첫번째 하트 위치 (잔량 확인)
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
    pyautogui.click(position[0])
    pyautogui.click(position[1])
    pyautogui.dragTo(position[2][0], position[2][1], position[2][2], button='left')
    pyautogui.click(position[0])

def closeWindows(pos_delay):
    '''각종 창 자동으로 닫아주기'''
    pyautogui.click(pos_delay[0][0])
    time.sleep(pos_delay[0][1])
    pyautogui.click(pos_delay[1][0])
    time.sleep(pos_delay[1][1])
    pyautogui.click(pos_delay[2][0])
    time.sleep(pos_delay[2][1])
    pyautogui.click(pos_delay[3][0])
    time.sleep(pos_delay[3][1])
    pyautogui.click(pos_delay[4][0])
    time.sleep(pos_delay[4][1])
    pyautogui.click(pos_delay[5][0])
    time.sleep(pos_delay[5][1])
    pyautogui.click(pos_delay[6][0])
    time.sleep(pos_delay[6][1])

def pushStartGame(pos_delay):
    '''게임 시작버튼 누르기'''
    pyautogui.click(pos_delay[0][0])
    time.sleep(pos_delay[0][1])
    pyautogui.click(pos_delay[1][0])
    time.sleep(pos_delay[1][1])

def isHeartEmpty(position):
    '''게임 플레이용 하트 잔량 체크하기'''
    os.system("scrot heart.png")
    heart_img = Image.open("heart.png")

    if heart_img.getpixel(position)[0] < 200:
        return True
    else:
        return False

width, height = pyautogui.size()
if not (width == 1920 and height == 1080):
    print("해상도를 1920 x 1080 으로 설정해주세요.")
    print(f"현재 해상도 : {width} x {height}")
else:
    print("쿠키런 매크로 시작")
    init(pause, failsafe)
    pushStartGame(startgame_pos)
    count = 0
    start_time = time.time()
    while count < setCount:
        inGame(ingame_pos)
        elapsed_time = time.time()
        if elapsed_time - start_time > playtime:
            for _ in range(4):
                unlockCardgame(card_pos, card_x, card_y, card_delay)
            closeWindows(window_pos)
            if isHeartEmpty(heart_pos):
                time.sleep(heart_delay)
            pushStartGame(startgame_pos)
            start_time = time.time()
            count += 1
            print(f"{count}판 완료")
