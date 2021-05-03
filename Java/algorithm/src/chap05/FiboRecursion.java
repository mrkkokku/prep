package chap05;

public class FiboRecursion {
	
	public static int fiboRecursion(int n) {
		if(n == 1)
			return 1;
		else if (n == 2)
			return 1;
		else 
			return fiboRecursion(n-1) + fiboRecursion(n-2);
	}
	
	public static void main(String[] args) {
		System.out.println("피보나치수열의 10번쨰 원소는? " + fiboRecursion(10));
	}

}
