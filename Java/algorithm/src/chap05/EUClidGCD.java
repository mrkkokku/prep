package chap05;

import java.util.Scanner;

public class EUClidGCD {
	
	static int gcd(int x, int y) {
		if (y == 0)
			return x;
		else
			return gcd(y, x % y); //여기서 왜 return이 빠지면 안되는지는 생각해보자
	}
	
	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		
		System.out.println("두 정수의 최대공약수를 구합니다.");
		
		System.out.print("정수를 입력하세요 : ");
		int x = stdIn.nextInt();
		
		System.out.print("정수를 입력하세요 : ");
		int y = stdIn.nextInt();
		
		System.out.println("최대공약수는  " + gcd(x, y) + "입니다.");
	}

}
