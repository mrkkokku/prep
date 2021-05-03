package chap05;

public class Fino {
	
	public static int fibo(int n) {
		int one = 1;
		int two = 1;
		int result = -1;
		
		if (n == 1)
			return one;
		else if (n == 2)
			return two;
		else {
			for( int i = 2; i < n; i++) {
				result = one + two;
				one = two;
				two = result;
			}
		}
		return result;
	}
	
	public static void main(String[] args) {
		System.out.println("�Ǻ���ġ������ 10���� ���Ҵ�? " + fibo(10));
	}

}
