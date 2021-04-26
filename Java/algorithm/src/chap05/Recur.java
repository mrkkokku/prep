package chap05;

import java.util.Scanner;

public class Recur {
	
	//재귀 함수
	/*
	 * 재귀함수가 작동하는 방식을 알아보는 클래스
	 * 아래의 함수는 recur(n-1)이 먼저 돌고,
	 * 그 내부에서 재귀처리되는 것들이 모두 돌아간 다음
	 * println 돌아가고 그 다음 recur(n-2)가 돌아가게 됨.	
	 */
	static void recur(int n) {
		if (n > 0) {
			recur(n-1);
			System.out.println(n);
			recur(n-2);
		}
	}
	
	public static void main(String[] args) {
		
		Scanner stdIn = new Scanner(System.in);
		
		System.out.print("정수를 입력하세요 : ");
		int x = stdIn.nextInt();
		
		recur(x);
	}

}
