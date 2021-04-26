package chap05;

import java.util.Scanner;
import chap04.IntStack;

public class RecurX1 {
	
	/*
	 * Recur클래스의 재귀적 표현을 제거하고
	 * 일반적으로 돌리는 방식을 써보는 것.
	 * 
	 * 스택을 이용해서 재귀를 쓰지않는건데,
	 * 출제 범위를 벗어난 내용인 듯 함
	 */
	static void recur(int n) {
		IntStack s = new IntStack(n);
		
		while (true) {
			if (n > 0) {
				s.push(n);
				n = n - 1;
				continue;
			}
			if (s.isEmpty() != true) {
				n = s.pop();
				System.out.println(n);
				n = n - 2;
				continue;
			}
			break;
		}
	}
	
	public static void main(String[] args) {
		
		Scanner stdIn = new Scanner(System.in);
		
		System.out.print("정수를 입력하세요 : ");
		int x = stdIn.nextInt();
		
		recur(x);
	}

}
