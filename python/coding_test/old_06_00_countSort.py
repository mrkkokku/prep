'''
계수정렬이라고도하는 count sort는
기존의 비교기반 정렬과 다르게
입력된 배열의 요소 중 가장 큰 요소의
값만큼의 크기를 가진 배열을
따로 만들어서, 
해당 값 자체가 곧 인덱스로
연결이 되도록 새로운 배열에
counting을 해서 넣는다.
새로운 배열에 기록된 그 counting자체가
정렬이 된 결과값이다.

이러한 점 때문에 
이 정렬 방법은
정수이고, 입력된 배열의 값이
성적 처럼 일정범위안에
(최소와 최대값의 차이가 크지 않은 경우가
유리하다)
'''

array = [7, 5, 9, 0,  3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# max값에 +1 해줘야 최대값이 들어갈 위치가 생김
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스값 증가

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

