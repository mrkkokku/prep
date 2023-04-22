package coding_test;

import java.util.Scanner;
import java.util.Arrays;

public class BigNum {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		// n m k를 공백 기준으로 구분해 입력받기
		int n = sc.nextInt();
		int m = sc.nextInt();
		int k = sc.nextInt();
		
		int[] arr = new int[n];
		for(int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		
		// 입력받은 수 정렬하기 -> Ascending임
		Arrays.sort(arr);
		
		int first = arr[n-1];
		int second = arr[n-2];
		
		int cnt = (m / (k + 1)) * k;
		cnt += m % (k + 1);
		
		int result = 0;
		result += cnt * first;
		result += (m - cnt) * second;
		
		System.out.println(result);
	}

}
