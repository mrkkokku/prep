
n = int(input())

data = []
for i in range(n):
    data.append(int(input()))
'''
data.sort()
data.reverse()
'''
result = sorted(data, reverse=True)

for i in result:
    print(i, end=' ')