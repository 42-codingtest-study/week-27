package b4_10773;
import java.util.*;

import zero_bufferedreader.Stack;
/*
 * 스택 구현 문제..
 * 1. 가장 먼저 arraylist, linkedlist로 stack 을 구현하려 했으나
 * 포기하고 stack 클래스 안에 new 로 구현해야 할지 고민하다가 막힘
 * 2. 구글에 자바로 스택 구현하는 방법 찾아보다가 배열은 개수 제한때문에 힘들고 
 * 링크드리스트는 노드를 구현해야 하는거때문에 또 의지 떨어짐
 * 3. 객프 수업에서 만들어놓은 스택 델리게이트 찾아서 arraylist로 extends되는 
 * 과제 파일을 찾아서 긁어옴
 * 4. 쓸데없는 empty, full, peek 없애고 필요한것만 남겼는데 인덱스 넘겨서 오류뜸
 * 5. else로 안빼서 틀렸다는 걸 나중에 알고 고쳤더니 성공!!!
 * 
 */
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		Stack<Integer> stack = new Stack<>();
		int k = s.nextInt();
		long sum = 0;
		for(int i = 0; i < k; i++) {
			int a = s.nextInt();
			
			if(a == 0) {
				stack.pop();
			}
			else stack.push(a);
		}
		for(int i : stack) {
			sum += i;
		}
		System.out.print(sum);
	}
}
class Stack<E> extends ArrayList<E> {

    public void push(E element) {
        add(element);
    }

    public E pop() {
        return remove(size() - 1);
    }
}
/*
public class stack {
	private int[] stack;

	void push(int a) {
		list.add(a);
	}
	void pop() {
		list.r
	}
}
*/
