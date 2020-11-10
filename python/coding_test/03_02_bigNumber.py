'''
주어진 배열에서 어떤 수를 M번더하여
가장 큰 수로 만드는 문제,
K번을 초과하여 더해질 수 없는 것이 특징

입력값은
5 8 3
2 4 5 4 6

윗줄 첫번째는 배열의 길이,
두번째는 M
세번째난 K
이런식이며 아랫줄은 배열을 뜻함
'''

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 배열에 넣기
data = list(map(int, input().split()))

data.sort()
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수
result = 0

while True:
    for i in range(k): #가장 큰 수를 k번 더하기 위해
        if m == 0:
            break
        result += first
        m -= 1 #더해질때 마다 1씩 빼기
    
    if m == 0:
        break
    result += second # 두번째 큰수를 더하기
    m -= 1

print(result)
