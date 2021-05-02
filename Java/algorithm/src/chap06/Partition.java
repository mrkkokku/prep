package chap06;

import java.util.Scanner;

public class Partition {
	
	static void swap(int[] a, int idx1, int idx2) {
		int t = a[idx1];
		a[idx1] = a[idx2];
		a[idx2] = t;
	}
	
	static void partition(int[] a, int n) {
		int pl = 0;     //���� Ŀ��
		int pr = n-1;   //������ Ŀ��
		int x = a[n/2]; // �ǹ��� �̰ɷ� ���
		
		do {
			while (a[pl] < x)
				pl++;
			while (a[pr] > x)
				pr--;
			if (pl <= pr)
				swap(a, pl++, pr--);
		} while (pl <= pr);
		
		System.out.println("�ǹ��� ���� " + x + "�Դϴ�.");
		
		System.out.println("�ǹ� ������ �׷�");
		for (int i = 0; i <= pl-1; i++)
			System.out.print(a[i] + " "); // a[0] ~ a[pl-1]
		System.out.println();
		
		if (pl > pr+1) {
			System.out.println("�ǹ��� ��ġ�ϴ� �׷�");
			for (int i = pr+1; i <= pl-1; i++)
				System.out.print(a[i] + " "); // a[pr+1] ~ a[pl-1]
			System.out.println();
		}
		
		System.out.println("�ǹ� �̻��� �׷�");
		for (int i = pr+1; i < n; i++)
			System.out.print(a[i] + " ");
		System.out.println();
	}
	
	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		
		System.out.println("�迭�� �����ϴ�");
		System.out.print("��ڼ� : ");
		int nx = stdIn.nextInt();
		int[] x = new int[nx];
		
		for (int i = 0; i < nx; i++) {
			System.out.print("x[" + i + "] : ");
			x[i] = stdIn.nextInt();
		}
		
		partition(x, nx); // �迭�� ũ�⸦ �޾ư��� �Ϳ� ����
	}

}

/* �̰� quickSort�� 1 pass�� ������ �Ͱ� ����
�迭�� �����ϴ�
��ڼ� : 5
x[0] : 2
x[1] : 4
x[2] : 3
x[3] : 1
x[4] : 5
�ǹ��� ���� 3�Դϴ�.
�ǹ� ������ �׷�
2 1 3 
�ǹ��� ��ġ�ϴ� �׷�
3 
�ǹ� �̻��� �׷�
3 4 5 
*/
