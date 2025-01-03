# cookierun_macro

간단한 `쿠키런 for kakao` 매크로 프로그램

---

## Feature

- 기본적인 인게임 매크로
- 각종 창 자동 넘김
- 매크로 방지용 창 자동 해제 기능 *(깜짝 미니게임! 같은 카드를 찾아라!)*
- 하트 소진시 자동대기 후 재진행
- 작동 전력 10W 이하 *(라즈베리파이 또는 저전력pc, 스마트폰 밝기 최저설정)*

---

## Usage

- 라즈비안 세로 해상도를 1080으로 고정하고, rdp를 이용해서 해상도 정확하게 원격 연결하기
- 라즈베리파이3 or 4, `GPU memory`를 `256MB 이상`으로 설정 권장
- 안드로이드폰 `화면자동꺼짐 해제` 또는 10분 이상으로 설정 (개발자 모드에서 화면켜짐상태 유지 체크)
- `scrcpy를 설치`하여 안드로이드폰 미러링 형식으로 작동하기(무선연결도 가능) *[설치 참고](https://syki66.github.io/blog/2021/10/27/scrcpy.html)*
- 터미널에서 아래 명령어를 이용하여 1프레임 전체화면으로 `scrcpy 실행`
    - `scrcpy --max-fps 1 --fullscreen -b 1M --crop 1080:1920:0:174`
- 앱이 튕길때를 대비해서 홈스크린에 절적한 위치값에 쿠키런 앱 놓고 좌표설정하기
- 쿠키런 설정
    - 왼쪽 : `슬라이드`, 오른쪽 : `점프`로 설정

---

## Caution

- 오작동이 나올 수도 있으니 사용하지 않는 폰으로 하는것을 권장
- 마우스가 Thonny 창 밖에 있어야 좌표 오작동을 안함
- pyautogui 설치할때 오류나면 아래 명령어 실행
```
sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
```


---

## Change Log

- [CHANGELOG.MD](https://github.com/syki66/cookierun-macro/blob/master/CHANGELOG.MD)

---

## Todo List

- 인게임 매크로 효율 높이기 (사용자 입력받기)
- 전체캡처를 범용으로 바꾸기

---
