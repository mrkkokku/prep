# 10진수 정수를 입력받아 2~36진수로 변환하여 출력하기
def card_conv(x: int, r: int) -> str:
    # 정수 x를 r진수로 변환한 뒤 그 수의 str 출력

    d = '' # 변환후의 문자열 들어갈 자리
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[ x % r ]
        x = x // r

    return d[::-1]

if __name__ == "__main__":
    print("10진수를 n진수로 변환합니다")

    while True:
        while True:
            no = int(input("변환할 값으로 음이 아닌 정수 입력 "))
            if no > 0:
                break
        
        while True:
            cd = int(input("어떤 진수로 변환할까요? : "))
            if 2 <= cd <= 36:
                break
        
        print(f"{cd}진수로는 {card_conv(no, cd)}입니다")

        retry = input("한번 더 변환할까요? Y/N ) " )
        if retry in {'N', 'n'}:
            break
