package coding_test;

import java.util.Arrays;
import java.util.Scanner;


public class Level01 {
	
	public static void bigNum() {
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
	
	public static void coins() {
		int n = 1260;
		int cnt = 0;
		int[] cointTypes = {500, 100, 50, 10};
		
		for(int i = 0; i < 4; i++) {
			int coin = cointTypes[i];
			cnt += n/coin;
			n %= coin;
		}
		
		System.out.println(cnt);
	}
	
	public static void findMin() {
		Scanner sc = new Scanner(System.in);
		
		// n, m을 공백기준으로 구분하여 입력 받기
		int n = sc.nextInt();
		int m = sc.nextInt();
		int result = 0;
		
		// 한 줄씩 입력 받아서 모두 확인
		for (int i = 0; i < n; i++) {
			
			int min_value = 10001;
			 
			for (int j = 0; j < m; j++) {
				int x = sc.nextInt();
				min_value = Math.min(min_value, x);
			}
			
			// 작은 애들 중에서 젤 큰 거 찾기
			result = Math.max(result, min_value);
		}
		System.out.println(result);
	}
	
	public static boolean hasadNum(int x) {
		/*
		양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
		예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
		자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.
		 */
		int sum = 0;
        
        String temp = String.valueOf(x);
        
        String[] tempList = temp.split("");
        
        for (String a : tempList) {
            sum += Integer.parseInt(a);
        }
        
        if (x % sum == 0) {
        	System.out.println("true");
            return true;
        } else {
        	System.out.println("false");
            return false;
        }
	}

	public static void main(String[] args) {
		System.out.println("=====시작=====\n");
		Level01.hasadNum(13);
		System.out.println("\n======끝======");
	}

}
