h = int(input())
m = 0
s = 0

result = 0

for i in range(h+1):
    for m in range(0, 60):
        for s in range(0, 60):
            if '3' in str(i) + str(m) + str(s):
                result += 1

print(result)