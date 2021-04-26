package chap04;

import java.util.Scanner;

/* 링버퍼 구현, 오래된 데이터를 버리는 용도로 사용.
 * 예를들면 데이터 수가 n인 배열에 계속 데이터가 입력될때
 * 가장 최근의 n개만 저장하고 나머지는 버리는 용도로 활용.
 * 이게 ring buffer
 */

public class LastNElements {
	
	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		
		final int N = 10; // 고정값
		int[] a = new int[N];
		int cnt = 0; //입력 받은 개수
		int retry;   // 한번더 할지 확인용
		
		System.out.println("정수를 입력하세요 : ");
		
		do {
			System.out.printf("%d번째 정수 : ", cnt + 1);
			a[cnt++ % N] = stdIn.nextInt();
			
			System.out.print("계속 할까요 ? 1 / 0 : ");
			retry = stdIn.nextInt();
		} while (retry == 1);
		
		int i = cnt - N;
		
		if (i < 0)
			i = 0;
		
		for(; i < cnt; i++)
			System.out.printf("%2d번째의 정수 = %d\n", i+1, a[i%N]); // a[i%N] 부분이 포인트,
		                                             // 데이터를 11개 입력했다면 출력은 2번째부터로 나오는데,
		                                             // 이 부분을 유심히 생각해보자
	}

}
