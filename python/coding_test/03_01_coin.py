# 거슬러줄 금액은 항상 10의 배수인 경우
money = int(input("거슬러 줘야하는 금액은? "))

coins = [ 500, 100, 50, 10 ]
count_coin = 0

for coin in coins:
    
    count_coin += money // int(coin)
    money %= int(coin)
    
print(count_coin)