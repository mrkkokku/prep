package chap04;

public class IntQueue {
	// �����۸� Ȱ���� ť �����
	private int max;  // ť�� �뷮
	private int front;// ù��° �����͸� ����Ű�� Ŀ��
	private int rear; // ������ ������ ������ ����Ű�� Ŀ��
	private int num; // ���� ������ �� -> front, rear�� �������
	                 // ť�� ����� ���������� ������ ���� ���� �ʿ���
	private int[] que; // ť ��ü
	
	public class EmptyIntQueueException extends RuntimeException {
		public EmptyIntQueueException() { }
	}
	
	public class OverflowIntQueueException extends RuntimeException {
		public OverflowIntQueueException() { }
	}
	
	// ������
	public IntQueue(int capacity) {
		num = front = rear = 0;
		max = capacity;
		try {
			que = new int[max];
		} catch (OutOfMemoryError e) {
			max = 0;
		}
	}
	
	public int enque(int x) throws OverflowIntQueueException {
		if (num >= max)
			throw new OverflowIntQueueException(); 
		que[rear++] = x;
		num++;
		
		if (rear == max)
			rear = 0; // rear�� 0���� ������������ rear�� �迭 �ִ�ġ�� �Ѿ� overflow �߻�
		
		return x;
	}
	
	public int deque() throws EmptyIntQueueException {
		if (num <= 0)
			throw new EmptyIntQueueException();
		
		int x = que[front++];
		num--;
		
		if (front == max)
			front = 0;
		
		return x;
	}
	
	public int peek() throws EmptyIntQueueException {
		if (num <= 0)
			throw new EmptyIntQueueException();
		return que[front];
	}
	
	// ť���� x�� �˻��Ͽ� �ε��� ��ȯ
	public int indexOf(int x) {
		for(int i = 0; i < num; i++) {
			int idx = (i + front) % max;
			if (que[idx] == x)
				return idx;
		}
		return -1;
	}
	
	public void clear() {
		num = front = rear = 0;
	}
	
	public int capacity() {
		return max;
	}
	
	public int size() {
		return num;
	}
	
	public boolean isEmpty() {
		return num <= 0;
	}
	
	public boolean isFull() {
		return num >= max;
	}
	
	// ť ���� ��� �����͸� front -> rear ������ ���
	public void dump() {
		if (num <= 0)
			System.out.println("ť�� ��� �ֽ��ϴ�");
		else {
			for (int i = 0; i < num; i++)
				System.out.print(que[(i + front) % max] + " ");
			System.out.println();
		}
	}
}
