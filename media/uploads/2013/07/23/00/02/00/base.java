//package myprog;

import java.util.Scanner;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.*;
import java.lang.*;


class base
{

public static void main(String args[]) throws IOException
{

	Scanner s = new Scanner(System.in);
	
	System.out.println("Enter the option");
	int opt = s.nextInt();
	
	switch(opt)
	{
		case 1:
			{
				DataInputStream in = new DataInputStream(System.in);
				System.out.println("Enter the value of n: ");
				int a = s.nextInt();
			//	int b= Integer.parseInt();
				System.out.println("hello World !" + a);
				break;
			}
		case 2:
			{
				int result = fact(5);
				System.out.println("The factorial of number is = " + result);
			}
		case 3:
			{
				String s2= "welcome";
				System.out.println("The string is = " + s2);
				String s1 ="welcome";
				System.out.println("The string is = " + s1);
				StringBuffer s4 = new StringBuffer("vijay");
				System.out.println("The string is = " + s4);
				s4.append("new");

				System.out.println("The string is = " + s4);
				BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
				int ma = Integer.parseInt( br.readLine());
				System.out.println(ma);	
				ma =  ma +30;
				System.out.println(ma);	
				int se = br.read();				
				System.out.println(se);	

			}
	}

}


static int fact(int fac)
{
	int i;
	int f =1;
	for(i=0;i<fac;i++)
		f= (fac-i)*f;
	return f;
}


}
