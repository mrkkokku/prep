package chap04;

public class IntQueue {
	// 링버퍼를 활용한 큐 만들기
	private int max;  // 큐의 용량
	private int front;// 첫번째 데이터를 가리키는 커서
	private int rear; // 마지막 투입한 데이터 가리키는 커서
	private int num; // 현재 데이터 수 -> front, rear가 같을경우
	                 // 큐가 빈건지 가득찬건지 구별을 돕기 위해 필요함
	private int[] que; // 큐 본체
	
	public class EmptyIntQueueException extends RuntimeException {
		public EmptyIntQueueException() { }
	}
	
	public class OverflowIntQueueException extends RuntimeException {
		public OverflowIntQueueException() { }
	}
	
	// 생성자
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
			rear = 0; // rear를 0으로 해주지않으면 rear가 배열 최대치를 넘어 overflow 발생
		
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
	
	// 큐에서 x를 검색하여 인덱스 반환
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
	
	// 큐 안의 모든 데이터를 front -> rear 순으로 출력
	public void dump() {
		if (num <= 0)
			System.out.println("큐가 비어 있습니다");
		else {
			for (int i = 0; i < num; i++)
				System.out.print(que[(i + front) % max] + " ");
			System.out.println();
		}
	}
}
