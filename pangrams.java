
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class solution {
	public static int count; 
	
    public static void main(String[] args) {
    	
    	
    	start();
    	test();
    	
    }  
    
    public static void start(){
    	Scanner scans = new Scanner(System.in);
    	String input = scans.nextLine();
    	String [] myList = input.trim().toLowerCase().split("");
    	

    	Set<String> uniqueNumbers = new HashSet<String>(Arrays.asList(myList));
    	uniqueNumbers.removeAll(Arrays.asList(""," ",null));
    //	System.out.println(uniqueNumbers); //this does work, better way?
    
    	for (int i = 0; i < uniqueNumbers.size(); i++)
    	    count +=1;
    	
    	
    }
    
    
    
    public static boolean test(){
    //	System.out.println(count);
    	if(count == 26){
    		System.out.println("pangram");

    		return true;	
    	}
    	else{
    		System.out.println("not pangram");

    		return false;}
    }
}
