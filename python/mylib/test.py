def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(fact(3))

print(gcd(192, 162))
'''
GCD Greatest common divisor

'''

INF = 99999999

graph = [
    [ 0, 7, 5 ],
    [ 7, 0, INF ],
    [5, INF, 0 ]
]

print(graph)
