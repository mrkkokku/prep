package chap06;

import java.util.Scanner;

public class Partition {
	
	static void swap(int[] a, int idx1, int idx2) {
		int t = a[idx1];
		a[idx1] = a[idx2];
		a[idx2] = t;
	}
	
	static void partition(int[] a, int n) {
		int pl = 0;     //왼쪽 커서
		int pr = n-1;   //오른쪽 커서
		int x = a[n/2]; // 피벗을 이걸로 잡고
		
		do {
			while (a[pl] < x)
				pl++;
			while (a[pr] > x)
				pr--;
			if (pl <= pr)
				swap(a, pl++, pr--);
		} while (pl <= pr);
		
		System.out.println("피벗의 값은 " + x + "입니다.");
		
		System.out.println("피벗 이하의 그룹");
		for (int i = 0; i <= pl-1; i++)
			System.out.print(a[i] + " "); // a[0] ~ a[pl-1]
		System.out.println();
		
		if (pl > pr+1) {
			System.out.println("피벗과 일치하는 그룹");
			for (int i = pr+1; i <= pl-1; i++)
				System.out.print(a[i] + " "); // a[pr+1] ~ a[pl-1]
			System.out.println();
		}
		
		System.out.println("피벗 이상의 그룹");
		for (int i = pr+1; i < n; i++)
			System.out.print(a[i] + " ");
		System.out.println();
	}
	
	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		
		System.out.println("배열을 나눕니다");
		System.out.print("요솟수 : ");
		int nx = stdIn.nextInt();
		int[] x = new int[nx];
		
		for (int i = 0; i < nx; i++) {
			System.out.print("x[" + i + "] : ");
			x[i] = stdIn.nextInt();
		}
		
		partition(x, nx); // 배열의 크기를 받아가는 것에 유의
	}

}

/* 이건 quickSort의 1 pass만 수행한 것과 같다
배열을 나눕니다
요솟수 : 5
x[0] : 2
x[1] : 4
x[2] : 3
x[3] : 1
x[4] : 5
피벗의 값은 3입니다.
피벗 이하의 그룹
2 1 3 
피벗과 일치하는 그룹
3 
피벗 이상의 그룹
3 4 5 
*/
