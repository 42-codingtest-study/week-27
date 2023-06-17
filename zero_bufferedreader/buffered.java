package zero_bufferedreader;

import java.util.ArrayList;
import java.util.StringTokenizer;
import java.io.*;
public class buffered {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		Stack<Integer> stack = new Stack<>();
		int k = Integer.parseInt(br.readLine());		
		StringTokenizer st;
		
		for(int i = 0; i < k; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			
			if(a == 0) {
				stack.pop();
			}
			else stack.push(a);
		}
		long sum = 0;
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