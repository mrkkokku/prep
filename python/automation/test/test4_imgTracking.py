import pyautogui as pg

button5location = pg.locateOnScreen('5.png') # 이미지가 있는 위치를 가져옵니다. 
print(button5location)

button5location = pg.locateOnScreen('5.png')
point = pg.center(button5location) # Box 객체의 중앙 좌표를 리턴합니다. 
print(point)