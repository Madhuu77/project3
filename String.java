package sample2;
import java.lang.String;
public class stringDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s1="gpt channasandra";
		String s2="GPT CHANNASANDRA";
		System.out.println("The string s1 is:"+s1);
		System.out.println("The string s2 is:"+s2);
		System.out.println("length of string s1 is:"+s1.length());
		System.out.println("length of string s2 is:"+s2.length());
	   System.out.println("The string s1 in Upper case:"+s1.toUpperCase());
	   System.out.println("The string s2 in Upper case:"+s2.toLowerCase());
	   System.out.println("The first occurence of a is at position :"+s1.indexOf('a'));
	   System.out.println("s1 equals to s2:"+s1.equals(s2));
	   System.out.println("s1 equals ignore case to s2:"+s1.equalsIgnoreCase(s2));
	   System.out.println("character at index of 6 is:"+s1.indexOf(6));
	   String s3=s1.substring(2,8);
         System.out.println("the extracted substring is:"+s3);
         System.out.println("Replacing a with b in s1:"+s1.replace('a', 'b'));
         System.out.println("After string concat:"+s1.concat(",Karnataka"));
         String s4="this is a book";
         System.out.println("The string s4 is:"+s4);
         System.out.println("After trim:"+s4.trim( ));
         int result=s1.compareTo(s2);
         System.out.println("after compare to");
         if(result==0)
        	 System.out.println(s1+"is equal to"+s2);
         else
        	 System.out.println(s1+" is smaller than:"+s2);
        	 
         
}}
