package chap04;

import java.util.Scanner;

/* ������ ����, ������ �����͸� ������ �뵵�� ���.
 * ������� ������ ���� n�� �迭�� ��� �����Ͱ� �Էµɶ�
 * ���� �ֱ��� n���� �����ϰ� �������� ������ �뵵�� Ȱ��.
 * �̰� ring buffer
 */

public class LastNElements {
	
	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		
		final int N = 10; // ������
		int[] a = new int[N];
		int cnt = 0; //�Է� ���� ����
		int retry;   // �ѹ��� ���� Ȯ�ο�
		
		System.out.println("������ �Է��ϼ��� : ");
		
		do {
			System.out.printf("%d��° ���� : ", cnt + 1);
			a[cnt++ % N] = stdIn.nextInt();
			
			System.out.print("��� �ұ�� ? 1 / 0 : ");
			retry = stdIn.nextInt();
		} while (retry == 1);
		
		int i = cnt - N;
		
		if (i < 0)
			i = 0;
		
		for(; i < cnt; i++)
			System.out.printf("%2d��°�� ���� = %d\n", i+1, a[i%N]); // a[i%N] �κ��� ����Ʈ,
		                                             // �����͸� 11�� �Է��ߴٸ� ����� 2��°���ͷ� �����µ�,
		                                             // �� �κ��� ������ �����غ���
	}

}
