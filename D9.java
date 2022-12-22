import java.util.*;
class D9
{
	public static void main(String args[])
	{
		Scanner ip = new Scanner(System.in);
		System.out.print("Enter the num: ");
		long a= ip.nextLong(),x;
		x=a;
		long b[]=new long[20];
		int k=0,s=0;
		while(a>0)
		{
			b[k++]=a%10;
			a=a/10;
		} 
		for(int i=0,j=k;i<k;i++,j--)
		{
			s+=Math.pow(b[i],j);
		//System.out.println(s);
		}
		if (s==x) {
			System.out.println("The given num is Disarium number");
		}
		else{
			System.out.println("The given num is not Disarium number");
		}
	}
}
