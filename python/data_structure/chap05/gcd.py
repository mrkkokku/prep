# 유클리드 호제법으로 최대 공약수 구하기
# Greatest Common Divisor

def gcd(x: int, y: int) -> int:
    ''' 정수값 x,y의 최대 공약수를 반환 '''
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

if __name__ == "__main__":
    print("두 정숫값의 최대 공약수를 구합니다.")

    x, y = map(int,input("x와 y의 값은 무엇입니까?\n").split())

    print(f"두 정숫값의 최대 공약수는 {gcd(x,y)}입니다.")