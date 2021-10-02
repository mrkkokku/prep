import pyautogui as pg

a = pg.alert('내용입니다', title = '제목입니다', button = 'OK')
print(a)

a = pg.confirm(text='내용입니다', title='제목입니다', buttons=['OK', 'Cancel'])
print(a)

a = pg.prompt(text='내용입니다', title='제목입니다', default='입력하세요')
print(a)
# 프롬프트에 입력한 값이 리턴 됨

a = pg.password(text='내용입니다', title='제목입니다', default='입력하세요', mask='*')
print(a)
# 프롬프트에 입력한 값이 리턴 됨. 입력할땐 마스킹처리 되어있음

