package chap06;

import java.util.Scanner;

public class HeapSort {
	
	static void swap(int[] a, int idx1, int idx2) {
		int t = a[idx1];
		a[idx1] = a[idx2];
		a[idx2] = t;
	}
	
	static void downHeap(int[] a, int left, int right) {
		int temp = a[left];  //�̰� �����ϰ� �ִ� �ִ밪
		int child;
		int parent;
		
		for (parent = left; parent < (right+1)/2; parent = child) {
			int cl = parent*2 + 1; // ���� �ڽ�
			int cr = cl + 1;       // ������ �ڽ�
			child = (cr <= right && a[cr] > a[cl]) ? cr : cl; // ū���� ���� ��带 �ڽĿ� ����
			if(temp >= a[child])
				break;
			a[parent] = a[child];
		}
		
		a[parent] = temp;
	}
	
	static void heapSort(int[] a, int n) {
		for (int i = (n-1)/2; i >= 0; i--) // a[i] ~ a[n-1]�� ������ �����
			downHeap(a, i, n-1);
		
		for (int i = n-1; i > 0; i--) {
			swap(a, 0 , i);  // ���� ū ��ҿ� ���� ���ĵ��� ���� �κ��� ������ ��� ����
			downHeap(a, 0, i-1); // a[0] ~ a[i-1]�� ������ �����
		}
	}
	
	public static void main(String[] ars) {
		Scanner stdIn = new Scanner(System.in);
		
		System.out.println("�� ����");
		System.out.print("��ڼ� : ");
		
		int nx = stdIn.nextInt();
		int[] x = new int[nx];
		
		for (int i = 0; i < nx; i++) {
			System.out.print("x[" + i + "] : ");
			x[i] = stdIn.nextInt();
		}
		
		heapSort(x, nx);
		
		System.out.println("������������ �����߽��ϴ�");
		for (int i = 0; i < nx; i++)
			System.out.println("x[" + i + "[ = " + x[i]);
	}

}
