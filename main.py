import pyautogui
import pyperclip
import time

# 안전모드 설정하기, 잘못되었을 경우 탈출구
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

URL = "https://gall.dcinside.com/board/write/?id=dog"

title = "랜선장터 진도 울금 구매 택배 주문 방법"

content = '''
<h3 style="font-size:1.3125em;margin:29px 0px 22px;padding:0px;clear:both;line-height:1.5;color:rgb(0,0,0);font-family:AppleSDGothicNeo, 'Noto Sans KR', sans-serif;text-align:center;"><span style="font-size:18pt;color:rgb(255,0,0);"><a href="https://dog.spares.co.kr/99"><span style="color:rgb(255,0,0);">랜선장터 진도 울금 구매 택배 주문 방법</span></a></span></h3><p style="margin-bottom:32px;font-size:0.9375em;line-height:2;color:rgb(85,85,85);font-family:AppleSDGothicNeo, 'Noto Sans KR', sans-serif;"><span style="font-size:12pt;">매주 수요일 밤 9시 30분 코로나19로 어려워진 지역 경제와 농어민에게 도움을 주기 위해 지역의 특산물을 소개하고 판매하는 KBS 2TV 랜선장터에서는 밭에서 나는 황금 ‘울금’ 판매를 위해 홍현희, 김동현, 이원일이 진도에 출격했습니다.</span></p>
<p style="margin-bottom:32px;font-size:0.9375em;line-height:2;color:rgb(85,85,85);font-family:AppleSDGothicNeo, 'Noto Sans KR', sans-serif;text-align:left;"><img src="https://dcimg2.dcinside.co.kr/viewimage.php?id=20a4d928e3dd&amp;no=24b0d769e1d32ca73ceb87fa1bd8233c52b981172b7c8ebcac8cd0542458df6dd3779fdf598b7b57dad76cf26c45aeb55234ad2b7cd072102f41208a0808525e7a954c29" style="clear:none;float:none;" alt="viewimage.php?id=20a4d928e3dd&amp;no=24b0d769e1d32ca73ceb87fa1bd8233c52b981172b7c8ebcac8cd0542458df6dd3779fdf598b7b57dad76cf26c45aeb55234ad2b7cd072102f41208a0808525e7a954c29"></p>
<p style="margin-bottom:32px;font-size:0.9375em;line-height:2;color:rgb(85,85,85);font-family:AppleSDGothicNeo, 'Noto Sans KR', sans-serif;"><span style="font-size:12pt;">랜선장터 진도 울금 구매 택배 주문 방법은 아래를 통해서 확인하실 수 있습니다.</span></p><h3 style="font-size:1.3125em;margin:29px 0px 22px;padding:0px;clear:both;line-height:1.5;color:rgb(0,0,0);font-family:AppleSDGothicNeo, 'Noto Sans KR', sans-serif;text-align:center;"><span style="font-size:18pt;color:rgb(255,0,0);"><a href="https://dog.spares.co.kr/99"><span style="color:rgb(255,0,0);">랜선장터 진도 울금 구매 택배 주문 방법</span></a></span></h3><p><br></p>
'''

screenwidth, screenheight = pyautogui.size()
print(screenwidth, screenheight)


#pyautogui.click(pyautogui.locateCenterOnScreen('search.png')) # 주소창 클릭
pyautogui.click(x=screenwidth/2, y=50) # 주소창 클릭

currentpX, currentpY = pyautogui.position()
print("주소창", currentpX, currentpY) #734 52

pyautogui.hotkey('ctrl', 'a')
pyautogui.press('backspace')
pyautogui.typewrite(URL)  # 주소 입력
pyautogui.press('enter')
time.sleep(3)


# 제목
pyautogui.click(pyautogui.locateCenterOnScreen('title.png'))
pyperclip.copy(title)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# 스크롤 내리기
#pyautogui.moveTo(x=1910, y=333)
#pyautogui.drag(0, 500, 1, button='left')
pyautogui.scroll(-500)

# HTML 버튼 클릭
pyautogui.click(pyautogui.locateCenterOnScreen('html.png'))

# 본문
pyautogui.doubleClick(pyautogui.locateCenterOnScreen('content.png'))
pyperclip.copy(content)
pyautogui.hotkey("ctrl", "v")

# 등록
pyautogui.click(pyautogui.locateCenterOnScreen('summit.png'))
