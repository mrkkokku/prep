package coding_test;

import java.util.Arrays;
import java.util.Scanner;


public class Level01 {
	
	public static void bigNum() {
		Scanner sc = new Scanner(System.in);
		
		// n m k�� ���� �������� ������ �Է¹ޱ�
		int n = sc.nextInt();
		int m = sc.nextInt();
		int k = sc.nextInt();
		
		int[] arr = new int[n];
		for(int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		
		// �Է¹��� �� �����ϱ� -> Ascending��
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
		
		// n, m�� ����������� �����Ͽ� �Է� �ޱ�
		int n = sc.nextInt();
		int m = sc.nextInt();
		int result = 0;
		
		// �� �پ� �Է� �޾Ƽ� ��� Ȯ��
		for (int i = 0; i < n; i++) {
			
			int min_value = 10001;
			 
			for (int j = 0; j < m; j++) {
				int x = sc.nextInt();
				min_value = Math.min(min_value, x);
			}
			
			// ���� �ֵ� �߿��� �� ū �� ã��
			result = Math.max(result, min_value);
		}
		System.out.println(result);
	}
	
	public static boolean hasadNum(int x) {
		/*
		���� ���� x�� �ϻ��� ���̷��� x�� �ڸ����� ������ x�� ���������� �մϴ�.
		���� ��� 18�� �ڸ��� ���� 1+8=9�̰�, 18�� 9�� ������ �������Ƿ� 18�� �ϻ��� ���Դϴ�.
		�ڿ��� x�� �Է¹޾� x�� �ϻ��� ������ �ƴ��� �˻��ϴ� �Լ�, solution�� �ϼ����ּ���.
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
		System.out.println("=====����=====\n");
		Level01.hasadNum(13);
		System.out.println("\n======��======");
	}

}
