/* Factorial of factorials  ---- Create a func that takes int n and returns factorial of factorials.
	I/p : fact_of_fact(4) --> 288
	4! * 3! * 2! * 1! -->288
*/

import java .util.*;
class D13
{
	public static int fact(int n)
	{
		if(n==0)
		{
			return 1;
		}
		else{
			return n * fact(n-1);
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(),f=1;
		for(int i=1;i<=a;i++)
		{
			f*=fact(i);
		}
		System.out.print(f);

	}
}