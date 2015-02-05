package hackerrank;

import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.util.Arrays;

public class lone{
	
	public static int least_ct = 101, x = 0;
	public static String var; 
	
	public static void main(String [] args){
	
	Scanner scan = new Scanner(System.in);
	x = scan.nextInt(); scan.nextLine(); 
	String input = scan.nextLine();	
	
	if(x > 100 || !(x >= 1) || x%2 != 1){ //accounts for constraints
	System.exit(0);
	}
	
    String [] items = input.split(" ");
    List<String> container = Arrays.asList(items);
    
    container = container.subList(0,x);
    
    	String temp;	
		for(int x=0; x<container.size(); x++){
			temp = container.get(x);
			int freq = Collections.frequency(container, temp);
			
				if(freq < least_ct){
					least_ct = freq;
					var = temp;
				}
		}
	System.out.println(var);
	//System.out.println(Arrays.toString(container.toArray()));
	scan.close();
	}	
} 
	
