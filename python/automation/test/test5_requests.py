import requests

response = requests.get('https://www.naver.com')

print(response.status_code) # 여기는 응답코드가 들어가있음
print(response.text) # text에는 html 코드가 들어가있음

print(type(response))