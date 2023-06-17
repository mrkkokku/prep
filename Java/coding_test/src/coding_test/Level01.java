package coding_test;

import java.util.Arrays;
import java.util.Collections;
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
	
	public static int[] numToArray(long n) {
		/*
		�ڿ��� n�� ������ �� �ڸ� ���ڸ� ���ҷ� ������ �迭 ���·� �������ּ���.
		������� n�� 12345�̸� [5,4,3,2,1]�� �����մϴ�.
		 */
		String str_n = String.valueOf(n);
        
        String[] strList = str_n.split("");
        int[] result = new int[strList.length];
        
        for(int i = 0; i < strList.length; i++){
            result[result.length - 1 - i] = Integer.parseInt(strList[i]);
        }
        
        
        for (long a : result) {
        	System.out.print(a + " ");
        }
        return result;
	}
	
	public static long intOrdering(long n) {
		/*
		�Լ� solution�� ���� n�� �Ű������� �Է¹޽��ϴ�.
		n�� �� �ڸ����� ū�ͺ��� ���� ������ ������ ���ο� ������ �������ּ���.
		������� n�� 118372�� 873211�� �����ϸ� �˴ϴ�.
		 */
		long answer = 0;
        String str_result = "";
        
        String temp = String.valueOf(n);
        
        String[] temp_list = temp.split("");
        
        Arrays.sort(temp_list, Collections.reverseOrder());
        
        for(int i = 0; i < temp_list.length; i++) {
            str_result += temp_list[i];
        }
        
        answer = Long.parseLong(str_result);
        
        return answer;
	}
	
	public static boolean handlingSTR(String s) {
		/*
		���ڿ� s�� ���̰� 4 Ȥ�� 6�̰�,
		���ڷθ� �������ִ��� Ȯ�����ִ� �Լ�,
		solution�� �ϼ��ϼ���.
		
		���� ��� s�� "a234"�̸� False�� �����ϰ� "1234"��� True�� �����ϸ� �˴ϴ�.

		���� ����
		s�� ���� 1 �̻�, ���� 8 ������ ���ڿ��Դϴ�.
		s�� ���� ���ĺ� ��ҹ��� �Ǵ� 0���� 9���� ���ڷ� �̷���� �ֽ��ϴ�.
		
		s	return
		"a234"	false
		"1234"	true
		*/
		boolean answer = true;
        
		if(!(s.length() == 4 || s.length() == 6)) {
			answer = false;
		} else {
			String[] temp = s.split("");
			
			for(int i = 0; i < temp.length; i++) {
				try {
					int isNum = Integer.valueOf(temp[i]);
				} catch (Exception e) {
					answer = false;
					break;
				}
			}
		}
		return answer;
	}

	public static void main(String[] args) {
		System.out.println("=====����=====\n");
		System.out.println(Level01.handlingSTR("a234"));
		System.out.println("\n======��======");
	}

}
