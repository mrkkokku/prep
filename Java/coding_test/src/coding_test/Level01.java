package coding_test;

import java.util.Arrays;
import java.util.Collections;
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
	
	public static int[] numToArray(long n) {
		/*
		자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
		예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
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
		함수 solution은 정수 n을 매개변수로 입력받습니다.
		n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
		예를들어 n이 118372면 873211을 리턴하면 됩니다.
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
		문자열 s의 길이가 4 혹은 6이고,
		숫자로만 구성돼있는지 확인해주는 함수,
		solution을 완성하세요.
		
		예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

		제한 사항
		s는 길이 1 이상, 길이 8 이하인 문자열입니다.
		s는 영문 알파벳 대소문자 또는 0부터 9까지 숫자로 이루어져 있습니다.
		
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
		System.out.println("=====시작=====\n");
		System.out.println(Level01.handlingSTR("a234"));
		System.out.println("\n======끝======");
	}

}
