import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

class test
{
    public static void main(String [] args) 
    {
        test s = new test();
        s.start();
	ArrayList<Integer> l1 = new ArrayList<Integer>();
	l1.add(1);
	l1.add(2);
	l1.add(3);

	for(int i : l1)
	{
		System.out.println("List elements" + i);
	}

	Iterator<Integer> ia = l1.iterator();
	while(ia.hasNext())
	{
		System.out.println("from iterator" + ia.next());
	}

	List<String> l2 = new ArrayList<String>(4);
	l2.add("vijay");
	l2.add(1,"james");



	System.out.println("List " + l2.get(1));



    }

    void start() 
    {
        int a = 3;
        int b = 4;
        System.out.print(" " + 7 + 2 + " ");
        System.out.print(a + b);
        System.out.print(" " + a + b + " ");
        System.out.print(foo() + a + b + " ");
        System.out.println(a + b + foo());
    }

    String foo() 
    {
        return "foo";
    }
}
